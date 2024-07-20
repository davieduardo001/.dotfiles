## Meus dotfiles

### 1. Instalação das Dependências Iniciais:

Certifique-se de instalar as seguintes dependências se estiver executando em uma instalação limpa:

- **openssh**
- **git**

Exemplo para instalar no Ubuntu:
```bash
sudo apt update
sudo apt install openssh-server git
```

Para Arch Linux:
```bash
sudo pacman -Syu openssh git
```

Para Windows e WSL:
Antes de prosseguir com a configuração, execute o **seguinte comando no PowerShell** (como administrador) para instalar as dependências iniciais (no path que instalou o .dotfiles):
```powershell
.\bin\winrc.ps1
```
Este script prepara o ambiente com as dependências necessárias no Windows. Após a instalação, execute o comando novamente e selecione a opção de instalação no WSL para configurar o ambiente de desenvolvimento no Windows Subsystem for Linux (WSL) para uso posterior.

### 2. Configuração do Ambiente Python

#### Criando e Ativando um Ambiente Virtual Python:

Para isolar dependências e configurações Python:

```bash
python3 -m venv venv
```

Para ativar o ambiente virtual:

```bash
source venv/bin/activate
```

Para desativar o ambiente virtual:

```bash
deactivate
```

---

## Utilização do SDKMAN! (para Java)

Aqui está um exemplo de como usar o SDKMAN! para gerenciar SDKs Java:

---

# Usando o SDKMAN! para Gerenciar SDKs Java

O SDKMAN! é uma ferramenta para gerenciar múltiplas versões do SDK Java em sistemas Unix. Ele facilita a instalação, atualização e troca entre diferentes versões do Java Development Kit (JDK).

## Instalação no Ubuntu, Arch Linux e WSL

Para instalar o SDKMAN!, siga estes passos:

1. **Instalação do SDKMAN!**:

   No terminal, execute o seguinte comando:

   ```sh
   curl -s "https://get.sdkman.io" | bash
   ```

   Este comando realiza o download e instalação do SDKMAN!.

2. **Inicialização do SDKMAN!**:

   Após a instalação, inicialize o SDKMAN! com o comando:

   ```sh
   source "$HOME/.sdkman/bin/sdkman-init.sh"
   ```

   Este comando configura as variáveis de ambiente do SDKMAN! na sessão atual do terminal.

3. **Verificação da Instalação**:

   Para verificar se o SDKMAN! foi instalado corretamente, execute o comando:

   ```sh
   sdk version
   ```

## Utilizando o SDKMAN! para Java

### Instalando um JDK Específico

Para instalar uma versão específica do JDK, utilize o comando `sdk install` seguido do nome e versão do JDK. Por exemplo:

```sh
sdk install java 11.0.11.hs-adpt
```

Substitua `java` por `maven`, `gradle`, ou outro SDK suportado pelo SDKMAN!.

### Alternando entre Versões de JDK

Você pode alternar entre diferentes versões do JDK usando o comando `sdk use`. Por exemplo, para usar o Java na versão 11:

```sh
sdk use java 11.0.11.hs-adpt
```

### Definindo uma Versão Padrão do JDK

Para definir uma versão padrão para o JDK, use o comando `sdk default`. Por exemplo, para definir o Java 11 como padrão:

```sh
sdk default java 11.0.11.hs-adpt
```

### Listando JDKs Instalados

Para listar todos os JDKs instalados e suas versões, use o comando `sdk list`:

```sh
sdk list java
```

Substitua `java` por `maven`, `gradle`, ou outro SDK para listar as versões instaladas desse SDK.

### Atualizando o SDKMAN!

Para atualizar o SDKMAN! e seu catálogo de versões disponíveis, use o comando `sdk update`:

```sh
sdk update
```

### Desinstalando um JDK

Para desinstalar um JDK, use o comando `sdk uninstall` seguido do nome e versão do JDK:

```sh
sdk uninstall java 11
```

---
