import numpy as np
import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import json
import csv
import pyperclip  

def verificar_dependencia_linear(vetores):
    matriz = np.array(vetores).T
    posto = np.linalg.matrix_rank(matriz)
    return "INDEPENDENTES" if posto == len(vetores) else "DEPENDENTES"

def combinacao_linear(vetores, coeficientes):
    resultado = np.zeros_like(vetores[0], dtype=float)
    for v, c in zip(vetores, coeficientes):
        resultado += c * np.array(v)
    return resultado

def atualizar_campos():
    for entrada in entradas_vetores:
        entrada.delete(0, tk.END)
    entrada_coef.delete(0, tk.END)
    label_resultado.config(text="")
    label_combinacao.config(text="")
    limpar_grafico()

def limpar_grafico():
    fig.clf()
    espaco = var_espaco.get()
    if espaco == "R2":
        ax = fig.add_subplot(111)
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.axhline(0, color='gray', linewidth=0.5)
        ax.axvline(0, color='gray', linewidth=0.5)
    else:
        ax = fig.add_subplot(111, projection='3d')
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.set_zlim(-10, 10)
    canvas.draw()

def desenhar_grafico(vetores, combinacao=None):
    limpar_grafico()
    espaco = var_espaco.get()
    cores = ['r', 'g', 'b']
    if espaco == "R2":
        ax = fig.add_subplot(111)
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.axhline(0, color='gray', linewidth=0.5)
        ax.axvline(0, color='gray', linewidth=0.5)
        for i, v in enumerate(vetores):
            ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color=cores[i % len(cores)])
        if combinacao is not None:
            ax.quiver(0, 0, combinacao[0], combinacao[1], angles='xy', scale_units='xy', scale=1, color='purple', linewidth=2)
    else:
        ax = fig.add_subplot(111, projection='3d')
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.set_zlim(-10, 10)
        for i, v in enumerate(vetores):
            ax.quiver(0, 0, 0, v[0], v[1], v[2], color=cores[i % len(cores)])
        if combinacao is not None:
            ax.quiver(0, 0, 0, combinacao[0], combinacao[1], combinacao[2], color='purple', linewidth=2)
    canvas.draw()

def calcular():
    try:
        espaco = var_espaco.get()
        dimensao = 2 if espaco == "R2" else 3
        vetores = []
        for entrada in entradas_vetores:
            texto = entrada.get()
            if texto.strip() == "":
                continue
            vetor = list(map(float, texto.split(',')))
            if len(vetor) != dimensao:
                messagebox.showerror("Erro", f"Todos os vetores devem ter {dimensao} componentes.")
                return
            vetores.append(vetor)

        if len(vetores) < 2:
            messagebox.showerror("Erro", "Digite pelo menos dois vetores.")
            return

        resultado_dep = verificar_dependencia_linear(vetores)
        label_resultado['text'] = f"Os vetores são linearmente {resultado_dep}."

        if entrada_coef.get():
            coeficientes = list(map(float, entrada_coef.get().split(',')))
            if len(coeficientes) != len(vetores):
                messagebox.showerror("Erro", "Número de coeficientes deve ser igual ao número de vetores.")
                return
            resultado_combinacao = combinacao_linear(vetores, coeficientes)
            if np.allclose(resultado_combinacao, np.zeros(dimensao)):
                label_combinacao['text'] = "É combinação linear!"
            else:
                label_combinacao['text'] = "Não é combinação linear."
        else:
            label_combinacao['text'] = "Sem combinação informada."

        desenhar_grafico(vetores, resultado_combinacao if entrada_coef.get() else None)

    except Exception as e:
        messagebox.showerror("Erro", f"Entrada inválida: {e}")

def gerar_texto():
    espaco = var_espaco.get()
    vetores = [entrada.get() for entrada in entradas_vetores if entrada.get().strip() != ""]
    coeficientes = entrada_coef.get()
    texto_final = f"Espaço Vetorial: {espaco}\n"
    for i, v in enumerate(vetores):
        texto_final += f"v{i+1} = {v}\n"
    texto_final += f"Dependência Linear: {label_resultado['text']}\n"
    texto_final += f"Combinação Linear: {label_combinacao['text']}\n"
    texto_final += f"Coeficientes: {coeficientes}\n"
    return texto_final

def exportar_txt():
    try:
        texto_final = gerar_texto()
        with open("resultado_vetores.txt", "w") as arquivo:
            arquivo.write(texto_final)
        messagebox.showinfo("Sucesso", "Resultado exportado como 'resultado_vetores.txt'")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao exportar: {e}")

def exportar_csv():
    try:
        espaco = var_espaco.get()
        vetores = [entrada.get() for entrada in entradas_vetores if entrada.get().strip() != ""]
        coeficientes = entrada_coef.get()
        with open("resultado_vetores.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Espaço Vetorial", espaco])
            for i, v in enumerate(vetores):
                writer.writerow([f"v{i+1}", v])
            writer.writerow(["Dependência Linear", label_resultado['text']])
            writer.writerow(["Combinação Linear", label_combinacao['text']])
            writer.writerow(["Coeficientes", coeficientes])
        messagebox.showinfo("Sucesso", "Resultado exportado como 'resultado_vetores.csv'")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao exportar: {e}")

def exportar_json():
    try:
        espaco = var_espaco.get()
        vetores = [entrada.get() for entrada in entradas_vetores if entrada.get().strip() != ""]
        coeficientes = entrada_coef.get()
        resultado = {
            "Espaco Vetorial": espaco,
            "Vetores": vetores,
            "Dependencia Linear": label_resultado['text'],
            "Combinacao Linear": label_combinacao['text'],
            "Coeficientes": coeficientes
        }
        with open("resultado_vetores.json", "w") as file:
            json.dump(resultado, file, indent=4)
        messagebox.showinfo("Sucesso", "Resultado exportado como 'resultado_vetores.json'")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao exportar: {e}")

def copiar_resultado():
    try:
        texto_final = gerar_texto()
        pyperclip.copy(texto_final)
        messagebox.showinfo("Sucesso", "Resultado copiado para a área de transferência.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao copiar: {e}")

def salvar_grafico():
    try:
        fig.savefig("grafico_vetores.png")
        messagebox.showinfo("Sucesso", "Gráfico salvo como 'grafico_vetores.png'")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar o gráfico: {e}")


janela = tk.Tk()
janela.title("Vetores - R² e R³ com Visualização e Exportação")


var_espaco = tk.StringVar(value="R2")
frame_espaco = tk.Frame(janela)
tk.Label(frame_espaco, text="Escolha o espaço vetorial:").pack(side=tk.LEFT)
tk.Radiobutton(frame_espaco, text="R²", variable=var_espaco, value="R2", command=atualizar_campos).pack(side=tk.LEFT)
tk.Radiobutton(frame_espaco, text="R³", variable=var_espaco, value="R3", command=atualizar_campos).pack(side=tk.LEFT)
frame_espaco.pack(pady=10)


tk.Label(janela, text="Digite até 3 vetores (ex: 1,2 ou 1,2,3):").pack()
entradas_vetores = []
for _ in range(3):
    entrada = tk.Entry(janela, width=30)
    entrada.pack()
    entradas_vetores.append(entrada)


tk.Label(janela, text="Coeficientes para combinação linear (ex: 2,-1,3):").pack()
entrada_coef = tk.Entry(janela, width=30)
entrada_coef.pack()


btn_calcular = tk.Button(janela, text="Calcular", command=calcular)
btn_calcular.pack(pady=10)


label_resultado = tk.Label(janela, text="", fg="blue")
label_resultado.pack()

label_combinacao = tk.Label(janela, text="", fg="green")
label_combinacao.pack()


fig = plt.figure(figsize=(6, 6))
canvas = FigureCanvasTkAgg(fig, master=janela)
canvas.get_tk_widget().pack()


frame_exportar = tk.Frame(janela)
tk.Button(frame_exportar, text="Exportar TXT", command=exportar_txt).pack(side=tk.LEFT, padx=5)
tk.Button(frame_exportar, text="Exportar CSV", command=exportar_csv).pack(side=tk.LEFT, padx=5)
tk.Button(frame_exportar, text="Exportar JSON", command=exportar_json).pack(side=tk.LEFT, padx=5)
tk.Button(frame_exportar, text="Copiar", command=copiar_resultado).pack(side=tk.LEFT, padx=5)
tk.Button(frame_exportar, text="Salvar Gráfico", command=salvar_grafico).pack(side=tk.LEFT, padx=5)
frame_exportar.pack(pady=10)

janela.mainloop()
