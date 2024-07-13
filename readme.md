# Meus dotfiles

## Primeira Instalação

### 1. Instalação das dependências caso esteja executando em uma instalação limpa:

Certifique-se de instalar as seguintes dependências se estiver executando em uma instalação limpa:

- **openssh**
- **git**

Exemplo para instalar no Ubuntu:
```bash
sudo apt update
sudo apt install openssh-server git
```

### 2. Torná-lo executável:

Após clonar ou baixar seus dotfiles, certifique-se de que o arquivo `dotfiles` seja executável:

```bash
chmod 755 ~/.dotfiles/bin/dotfiles
```

---

## Utilizção do SDK

Claro, aqui está um exemplo de README em português para guiar os usuários sobre como usar o SDKMAN! para gerenciar SDKs:

---

# Usando o SDKMAN! para Gerenciar SDKs

O SDKMAN! é uma ferramenta para gerenciar múltiplos Kits de Desenvolvimento de Software (SDKs) em sistemas baseados em Unix. Ele simplifica a instalação, atualização e troca entre diferentes versões de SDKs como Java, Maven, Gradle, e outros.

## Instalação

Para instalar o SDKMAN!, siga os seguintes passos:

1. **Instale o SDKMAN!**:

   Abra seu terminal e execute o seguinte comando:

   ```sh
   curl -s "https://get.sdkman.io" | bash
   ```

   Este comando faz o download e instala o SDKMAN!.

2. **Inicialize o SDKMAN!**:

   Após a instalação ser concluída, inicialize o SDKMAN! com o seguinte comando:

   ```sh
   source "$HOME/.sdkman/bin/sdkman-init.sh"
   ```

   Este comando configura as variáveis de ambiente do SDKMAN! na sua sessão atual do terminal.

3. **Verifique a Instalação**:

   Para verificar se o SDKMAN! foi instalado corretamente, você pode verificar a versão:

   ```sh
   sdk version
   ```

## Usando o SDKMAN!

### Instalando SDKs

Para instalar um SDK específico, use o comando `sdk install` seguido do nome e versão do SDK. Por exemplo, para instalar o Java:

```sh
sdk install java 11.0.11.hs-adpt
```

Substitua `java` por `maven`, `gradle`, ou qualquer outro SDK suportado pelo SDKMAN!.

É recomendável preferir versões que usem o HotSpot da OpenJDK, indicado pelo sufixo `hs-adpt`, como `11.0.11.hs-adpt`, por serem baseadas em uma implementação estável e amplamente utilizada do Java Virtual Machine (JVM).

### Alternando entre Versões de SDK

Você pode alternar entre diferentes versões dos SDKs instalados usando o comando `sdk use`. Por exemplo, para usar o Java na versão 11:

```sh
sdk use java 11.0.11.hs-adpt
```

### Definindo uma Versão Padrão de SDK

Para definir uma versão padrão para um SDK, use o comando `sdk default`. Por exemplo, para definir o Java 11 como padrão:

```sh
sdk default java 11.0.11.hs-adpt
```

### Listando os SDKs Instalados

Para listar todos os SDKs instalados e suas versões, use o comando `sdk list`:

```sh
sdk list java
```

Substitua `java` por `maven`, `gradle`, ou outro SDK para listar as versões instaladas desse SDK.

### Atualizando o SDKMAN!

Para atualizar o SDKMAN! e seu catálogo de versões disponíveis, use o comando `sdk update`:

```sh
sdk update
```

### Desinstalando SDKs

Para desinstalar um SDK, use o comando `sdk uninstall` seguido do nome e versão do SDK:

```sh
sdk uninstall java 11
```

Essas instruções ajudam a gerenciar diferentes versões de SDKs de forma eficiente usando o SDKMAN!. Certifique-se de verificar a disponibilidade das versões e preferir aquelas que são baseadas no HotSpot da OpenJDK (`hs-adpt`) para uma experiência de desenvolvimento estável e compatível com a maioria das aplicações Java.