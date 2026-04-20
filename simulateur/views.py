from django.shortcuts import render
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import base64
import io


def simuler(request):
    graphique = None
    params = None

    if request.method == "POST":
        distribution = request.POST.get("distribution")
        n = int(request.POST.get("n"))
        repetitions = int(request.POST.get("repetitions"))

        # Récupérer les paramètres optionnels
        lambda_val = float(request.POST.get("lambda_val", 1))
        p_val = float(request.POST.get("p_val", 0.5))

        moyennes = []

        for i in range(repetitions):
            if distribution == "uniforme":
                echantillon = np.random.uniform(0, 1, n)
            elif distribution == "exponentielle":
                echantillon = np.random.exponential(1 / lambda_val, n)
            elif distribution == "binomiale":
                echantillon = np.random.binomial(10, p_val, n)
            elif distribution == "poisson":
                echantillon = np.random.poisson(lambda_val, n)

            moyennes.append(np.mean(echantillon))

        moyennes = np.array(moyennes)

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.hist(
            moyennes,
            bins=40,
            density=True,
            color="steelblue",
            edgecolor="white",
            alpha=0.8,
            label="Moyennes simulées",
        )

        mu = np.mean(moyennes)
        sigma = np.std(moyennes)
        x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 200)
        courbe = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(
            -0.5 * ((x - mu) / sigma) ** 2
        )
        ax.plot(x, courbe, color="red", linewidth=2, label="Normale théorique")

        ax.set_title("Théorème Central Limite — Distribution des moyennes")
        ax.set_xlabel("Moyenne des échantillons")
        ax.set_ylabel("Densité")
        ax.legend()
        plt.tight_layout()

        buffer = io.BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
        plt.close()

        graphique = image_base64
        params = {
            "distribution": distribution,
            "n": n,
            "repetitions": repetitions,
            "moyenne": round(float(mu), 4),
            "ecart_type": round(float(sigma), 4),
            "lambda_val": lambda_val,
            "p_val": p_val,
        }

    return render(
        request,
        "simulateur/index.html",
        {
            "graphique": graphique,
            "params": params,
        },
    )
