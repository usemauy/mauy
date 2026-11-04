# MAUY Fitness — loja + painel (HTML/CSS/JS puros, sem build)

```
index.html          Loja (carrossel, vitrine, carrinho, frete, cupom, checkout simulado)
admin/index.html    Painel (visão geral, produtos, pedidos, cupons, exportar dados)
data/site.json      Nome, WhatsApp, tema, banners, frete por faixa de CEP, cupons
data/produtos.json  Catálogo inicial
```

## Testar localmente
A loja lê os JSON com `fetch`, então sirva a pasta:

```
python3 -m http.server 8080
```

Loja: http://localhost:8080 — Painel: http://localhost:8080/admin/

## Publicar
- **GitHub Pages:** suba a pasta, vá em Settings → Pages e escolha a branch `main`.
- **Vercel:** Add New → Project, importe o repositório e faça o Deploy (sem framework nem build). O `index.html` deve ficar na raiz do projeto.

## Como os dados funcionam
Produtos, cupons e pedidos editados no painel ficam no `localStorage` do navegador
(`mauy_produtos`, `mauy_site`, `mauy_pedidos`). A loja lê essas mesmas chaves,
então as mudanças aparecem na hora, mas só naquele navegador.

Para tornar as mudanças definitivas para todos os visitantes:
1. Painel → **Dados / Exportar** → baixe `produtos.json` e `site.json`.
2. Substitua os arquivos em `data/` e faça o commit.

## Editar direto nos JSON
- **Banners:** `banners` em `data/site.json`.
- **Frete:** `frete.regras` (faixas de CEP, a primeira que casar vale), `frete.gratisAcima` e `frete.retirada`.
- **Cores:** `tema` em `data/site.json`.

## Atenção
- O painel não tem login. No site público, qualquer pessoa abre `/admin/`, mas só altera dados do próprio navegador.
- Pedidos e estoque do checkout são simulados e não passam por servidor.
- Para restaurar os dados originais: painel → Dados / Exportar → Restaurar.
