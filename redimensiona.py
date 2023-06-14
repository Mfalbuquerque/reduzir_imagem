import os 
from PIL import Image

def eh_imagem(nome_arquivo):
    if nome_arquivo.endswith('png') or nome_arquivo.endswith('jpg'):
        return True
    return False

def reduzir(input_dir, output_dir, ext='.jpeg'):
    lista_arquivo = [nome for nome in os.listdir(input_dir) if eh_imagem(nome)]
    for nome in lista_arquivo:
        imagem = Image.open(os.path.join(input_dir, nome))
        redimensionada = imagem.resize((960,960))
        nome_sem_ext = os.path.splitext(nome)[0]  
        redimensionada.save(os.path.join(output_dir, nome_sem_ext + ext))
        #print(lista_arquivo)   


if __name__ == "__main__":
    diretorio = r"diretorio"

    reduzir(diretorio, diretorio)

#se quiser mudar a extensão é só colocar a variavel acima assim 
# reduzir(diretorio, diretorio, 'png' ) <> onde png é a extensão desejada