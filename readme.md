# Extrator de legenda

![Srt extractor](thumb.png "Srt extractor")

### Requisitos:

1. **ffmpeg** instalado e nas variáveis de ambiente.

	Baixar e instalar:
	https://ffmpeg.org/download.html

	Adicionar no path:
	https://www.java.com/pt_BR/download/help/path.xml

2. **Python 3** instalado

	https://www.python.org/

------------

### Como rodar

Com tudo instalado, arrastando o vídeo para cima do arquivo `01.extract_srt.py` você extrairá o srt bruto (com tags e timestamps) na pasta de origem.

Arraste o srt resultante para cima do arquivo `02.clear_srt.py` para limpar o arquivo gerando um txt na pasta de origem.

------------

### Limpador de srt

**Crédito**:

https://gist.github.com/ndunn219/62263ce1fb59fda08656be7369ce329b
