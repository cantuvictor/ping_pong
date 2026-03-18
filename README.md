# 🏓 Pong em Python (Pygame)

Este projeto é uma recriação do clássico jogo **Pong**, desenvolvido em Python utilizando a biblioteca Pygame.

O objetivo foi não apenas fazer o jogo funcionar, mas também organizar o código de forma mais limpa, separando responsabilidades e deixando o projeto mais fácil de entender e evoluir.

---

## 🎮 Como funciona

* Você controla a raquete da esquerda com as teclas:

  * ↑ (seta para cima)
  * ↓ (seta para baixo)
* A raquete da direita é controlada automaticamente (IA simples)
* O jogo conta pontos sempre que a bola passa por um dos lados

---

## 🧱 Organização do projeto

O código foi dividido em partes para facilitar a leitura e manutenção:

```
ping_pong/
│
├── main.py
│
├── dominio/
│   ├── bola.py
│   ├── raquete.py
│   └── placar.py
│
├── servicos/
│   └── jogo.py
│
├── interface/
│   └── menu_principal.py
│
└── configuracoes/
    └── constantes.py
```

Cada arquivo tem uma responsabilidade específica, por exemplo:

* `bola.py` → controla a movimentação da bola
* `raquete.py` → controla as raquetes
* `placar.py` → gerencia a pontuação
* `jogo.py` → controla a lógica do jogo
* `menu_principal.py` → exibe o menu inicial

---

## 🛠️ O que foi feito

* Criação do jogo Pong funcional
* Separação do código em múltiplos arquivos
* Organização por responsabilidades
* Aplicação de boas práticas de código
* Padronização de nomes e estrutura

---

