# Meus dotfiles

## 1. Instalação das dependências caso esteja executando em uma instalação limpa:

Certifique-se de instalar as seguintes dependências se estiver executando em uma instalação limpa:

- **openssh**
- **git**

Exemplo para instalar no Ubuntu:
```bash
sudo apt update
sudo apt install openssh-server git
```

## 2. Torná-lo executável:

Após clonar ou baixar seus dotfiles, certifique-se de que o arquivo `dotfiles` seja executável:

```bash
chmod 755 ~/.dotfiles/bin/dotfiles
```

---

Este README fornece instruções básicas para configurar e executar seus dotfiles, garantindo que as dependências necessárias sejam instaladas e que o binário seja configurado corretamente para execução.