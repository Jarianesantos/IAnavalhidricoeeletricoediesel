from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="Sistema Inteligente de Propulsão Naval",
    description="IA para otimização energética em embarcações híbridas diesel-elétricas",
    version="1.0"
)

# ==========================================
# HOME
# ==========================================
@app.get("/", response_class=HTMLResponse)
def home():

    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>IA Naval</title>

        <style>

            body{
                font-family: Arial;
                background: #000080;
                color: white;
                margin: 0;
                padding: 0;
            }

            .container{
                width: 90%;
                margin: auto;
                padding: 40px;
            }

            h1{
                color: #gray;
            }

            .card{
                background: #367cdd;
                padding: 50px;
                border-radius: 12px;
                margin-top: 50px;
            }

            button{
                background: #367cdd;
                border: none;
                padding: 12px;
                border-radius: 8px;
                cursor: pointer;
                font-size: 16px;
            }

            input{
                width: 100%;
                padding: 10px;
                margin-top: 10px;
                border-radius: 8px;
                border: none;
            }

        </style>
    </head>

    <body>

        <div class="container">

            <h1> Sistema Inteligente de Propulsão Naval</h1>

            <p>
            Aplicação de Inteligência Artificial para otimização
            energética em sistemas híbridos diesel-elétricos.
            </p>

            <div class="card">

                <h2>Simulação Energética</h2>

                <label>Velocidade do Navio</label>
                <input type="number" id="velocidade" value="20">

                <label>Carga Operacional (%)</label>
                <input type="number" id="carga" value="70">

                <button onclick="calcular()">
                    Calcular Demanda
                </button>

                <h3 id="resultado"></h3>

            </div>

        </div>

        <script>

            async function calcular(){

                let velocidade =
                    document.getElementById("velocidade").value;

                let carga =
                    document.getElementById("carga").value;

                let response = await fetch(
                    `/energia?velocidade=${velocidade}&carga=${carga}`
                );

                let data = await response.json();

                document.getElementById("resultado").innerHTML =
                    "Demanda: " +
                    data.demanda_kw.toFixed(2) +
                    " kW";
            }

        </script>

    </body>
    </html>
    """

    return html_content


# ==========================================
# API PREDICT
# ==========================================
@app.get("/predict")
def predict():

    return {
        "consumo": "125 kWh",
        "emissao": "32 kg CO2",
        "status": "Sistema otimizado"
    }


# ==========================================
# CÁLCULO ENERGÉTICO
# ==========================================
@app.get("/energia")
def energia(velocidade: float, carga: float):

    demanda = velocidade * carga * 0.25

    diesel = demanda * 0.65
    bateria = demanda * 0.35

    return {
        "demanda_kw": demanda,
        "diesel_kw": diesel,
        "bateria_kw": bateria,
        "status": "Otimização concluída"
    }