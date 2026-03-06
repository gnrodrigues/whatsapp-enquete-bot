# 📊 WhatsApp Poll Bot (Python + Selenium)

Bot em **Python** que cria **enquetes automaticamente no WhatsApp Web** usando **Selenium**.

O script abre o WhatsApp Web, permite login via **QR Code**, acessa um grupo e cria uma enquete automaticamente.

Ideal para:

- organizar eventos em grupo
- votações rápidas
- automação de tarefas repetitivas

---

# 🚀 Funcionalidades

- Login automático no WhatsApp Web
- Autenticação via **QR Code**
- Criação automática de **enquetes**
- Configuração fácil de pergunta e opções
- Uso de **perfil persistente do Chrome** (não precisa logar toda vez)

---

# 🛠 Tecnologias utilizadas

- Python 3
- Selenium
- WebDriver Manager
- WhatsApp Web

---

# 📂 Estrutura do projeto

- whatsapp-poll-bot
│
├── bot.py
├── requirements.txt
├── README.md
└── .gitignore


---

# 📋 Pré-requisitos

Antes de rodar o projeto, você precisa ter instalado:

- **Python 3.9 ou superior**
- **Google Chrome**


Verifique sua versão do Python:

bash
python --version
---

# 📥 Instalação

Clone o repositório:

git clone https://github.com/gnrodrigues/whatsapp-enquete-bot.git

Entre na pasta do projeto:

cd whatsapp-enquete-bot
# 📦 Instalar dependências

Instale as bibliotecas necessárias:

pip install -r requirements.txt

O arquivo requirements.txt contém:

selenium
webdriver-manager
# ▶️ Executar o bot

Para executar o script:

python bot.py

O navegador abrirá automaticamente.

# 🔐 Login no WhatsApp (QR Code)

Quando o navegador abrir o WhatsApp Web, aparecerá um QR Code.

Para autenticar:

Abra o WhatsApp no celular

Vá em Dispositivos conectados

Clique em Conectar dispositivo

Escaneie o QR Code exibido no navegador

Após o primeiro login, a sessão será salva no perfil do Chrome criado pelo script.

Isso significa que não será necessário escanear novamente em execuções futuras.

# ⚙️ Configuração da enquete

Edite as variáveis no início do arquivo bot.py.

Nome do grupo
NOME_GRUPO = "Happy Hour"
Pergunta da enquete
PERGUNTA = "Happy Hour Hoje?"
Opções da enquete
OPCOES = [
    "Vou",
    "Talvez",
    "Não vou"
]

Você pode adicionar mais opções conforme necessário.

# 🔎 Como o script funciona

O bot executa os seguintes passos automaticamente:

Abre o WhatsApp Web

Aguarda login via QR Code

Busca o grupo configurado

Abre o menu de anexos

Seleciona a opção Poll

Preenche a pergunta

Insere as opções da enquete

Envia a enquete

# ⚠️ Observações importantes

Este projeto utiliza automação no WhatsApp Web.

Use com moderação, pois automações podem violar os Termos de Serviço do WhatsApp.

Este projeto é destinado para:

estudos

automação pessoal

experimentação com Selenium

# 🔮 Possíveis melhorias futuras

Algumas melhorias que podem ser implementadas:

envio para múltiplos grupos

leitura da enquete a partir de arquivo JSON

agendamento automático de enquetes

interface de linha de comando

interface gráfica

# 👨‍💻 Autor

Gabriel Nava Rodrigues

# ⭐ Contribuição

Pull requests são bem-vindos.

Se o projeto foi útil para você, considere dar uma ⭐ no repositório.

# ▶️ Como usar BAT

Edite arquivo run_bot.bat na raiz do projeto.

Substitua o caminho abaixo pelo caminho real da pasta do projeto:

C:\caminho\para\whatsapp-enquete-bot

Exemplo:

C:\Users\Gabriel\Documents\whatsapp-enquete-bot

Execute o bot com duplo clique no arquivo:

run_bot.bat

O script irá:

acessar a pasta do projeto

executar bot.py

abrir o navegador automaticamente

# 💡 Vantagens

execução rápida

não precisa abrir terminal

mais fácil para usuários iniciantes

útil para automação ou agendamento no Windows

# ⏰ Execução agendada (opcional)

O arquivo .bat também pode ser usado no Agendador de Tarefas do Windows para executar o bot automaticamente em horários específicos.

Exemplo de uso:

enviar enquete diária

criar votações recorrentes em grupos

automatizar organização de eventos

