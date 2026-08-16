import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def gerar_e_plotar_mapa(M, N):
    total_celulas = M * N
    qtd_obstaculos = int(0.20 * total_celulas)
    qtd_sujeira = int(0.10 * total_celulas)

    
    mapa_flat = np.zeros(total_celulas, dtype=np.int8)

    mapa_flat[:qtd_obstaculos] = 1
    mapa_flat[qtd_obstaculos:qtd_obstaculos + qtd_sujeira] = 2

    np.random.shuffle(mapa_flat)

    indices_validos = np.where(mapa_flat != 1)[0]
    
    idx_robo = np.random.choice(indices_validos)
    robo_linha, robo_coluna = divmod(idx_robo, N)

    mapa = mapa_flat.reshape((M, N))

 
    cmap = mcolors.ListedColormap(['white', 'black', 'saddlebrown'])
    bounds = [-0.5, 0.5, 1.5, 2.5]
    norm = mcolors.BoundaryNorm(bounds, cmap.N)

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(mapa, cmap=cmap, norm=norm)

    
    if max(M, N) <= 150:
       
        ax.set_xticks(np.arange(-0.5, N, 1), minor=True)
        ax.set_yticks(np.arange(-0.5, M, 1), minor=True)
        ax.grid(which="minor", color="gray", linestyle='-', linewidth=0.5)
        ax.tick_params(which="minor", size=0)
        
        
        ax.set_xticks(np.arange(0, N, max(1, N//10))) 
        ax.set_yticks(np.arange(0, M, max(1, M//10)))
    else:
       
        ax.axis('off')
       

    
    tamanho_robo = 300 if max(M, N) <= 100 else (50 if max(M, N) <= 1000 else 10)
    ax.scatter(robo_coluna, robo_linha, c='blue', s=tamanho_robo, label='Robô', edgecolors='white', zorder=5)

    ax.set_title(f"Mapa do Robô - {M}x{N}")
    
    import matplotlib.patches as mpatches
    patch_livre = mpatches.Patch(color='white', label='Livre', ec='gray')
    patch_obs = mpatches.Patch(color='black', label='Obstáculo')
    patch_suj = mpatches.Patch(color='saddlebrown', label='Sujeira')
    handles, labels = ax.get_legend_handles_labels() 
    
    ax.legend(handles=[patch_livre, patch_obs, patch_suj, handles[0]], 
              loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=4)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("--- Gerador de Mapa do Robô ---")
    try:
        M = int(input("Digite o número de linhas (M): "))
        N = int(input("Digite o número de colunas (N): "))
        gerar_e_plotar_mapa(M, N)
    except ValueError:
        print("Por favor, digite apenas números inteiros válidos.")