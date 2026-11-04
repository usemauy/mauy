# MAUY Fitness — loja + painel (HTML/CSS/JS puros, sem build)

```text
index.html          Redireciona para a loja do cliente
cliente/index.html  Loja (vitrine, banners, busca, sacola e checkout via WhatsApp)
admin/index.html    Painel (produtos, cupons, pedidos e exportação de dados)
site.json           Configuração da loja
produtos.json       Catálogo de produtos
```

## Testar localmente
A loja e o painel carregam os arquivos JSON com `fetch`, então sirva a raiz do projeto:

```bash
python3 -m http.server 8080
```

- Loja: http://localhost:8080/ ou http://localhost:8080/cliente/
- Painel: http://localhost:8080/admin/

## Publicar
- **GitHub Pages:** publique a raiz do repositório na branch `main`.
- **Vercel:** importe o repositório e faça o deploy (sem framework nem build).

## Como os dados funcionam
O painel salva produtos e configurações no `localStorage` (`mauy_produtos`, `mauy_site`, `mauy_pedidos`). A loja lê as mesmas chaves para mostrar as alterações nesse navegador. O carrinho fica em `mauy_carrinho`.

Para publicar alterações para todos os visitantes, exporte `site.json` e `produtos.json` no painel e substitua os arquivos na raiz do repositório.

## Atenção
O painel não tem autenticação. Os dados alterados no painel ficam no navegador atual até serem exportados e publicados. Pedidos e estoque não são processados por um servidor.
