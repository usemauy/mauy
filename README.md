# MAUY — Loja virtual e painel administrativo

Projeto da loja virtual MAUY com painel administrativo integrado. A estrutura reúne a vitrine, as configurações da loja, o catálogo de produtos e os diretórios destinados às imagens.

## Estrutura do projeto

```text
MAUY/
├── index.html          # Loja virtual e painel administrativo
├── dados.json          # Dados consolidados consumidos pela vitrine
├── site.json           # Configurações da marca e da loja
├── produtos.json       # Catálogo de produtos
├── LEIA-ME.txt         # Orientações rápidas
└── img/
    ├── site/           # Logos, favicon, banners e imagens institucionais
    └── produtos/       # Fotografias dos produtos
```

## Para que serve cada arquivo?

- **`index.html`**: contém a loja virtual e o painel administrativo integrado.
- **`site.json`**: guarda as configurações da loja, como identidade visual e informações institucionais.
- **`produtos.json`**: guarda o catálogo de produtos e seus dados.
- **`dados.json`**: reúne os dados no formato utilizado pela vitrine da loja.

O painel foi preparado para trabalhar com esses arquivos. Ao utilizar a publicação configurada no painel, confira se os três JSONs e as imagens foram enviados ao repositório.

## Adicionando imagens

Coloque os arquivos nos diretórios correspondentes:

- `img/site/`: logos, favicon, banners e imagens institucionais.
- `img/produtos/`: fotos dos produtos.

Formatos recomendados:

- **Fotografias e banners:** JPG/JPEG ou WebP.
- **Imagens com transparência:** PNG ou WebP.
- **Logos e ícones vetoriais:** SVG ou PNG.

Adicionar uma imagem à pasta não a exibe automaticamente na loja. Ela também precisa estar selecionada/cadastrada no painel ou referenciada no JSON correspondente, com o caminho correto.

## Como começar

1. Faça o upload de todos os arquivos e pastas deste projeto para a raiz do repositório GitHub.
2. Mantenha `index.html`, `dados.json`, `site.json` e `produtos.json` na mesma raiz.
3. Abra a loja e o painel pelo endereço publicado.
4. Cadastre as informações da marca e os produtos pelo painel administrativo.
5. Antes de publicar alterações, configure e confira a integração com o GitHub no painel.
6. Se utilizar a Vercel, importe/conecte este mesmo repositório e publique a partir da raiz do projeto.

## Atenção

- Os arquivos JSON precisam manter sintaxe válida. Não inclua comentários dentro deles.
- Não renomeie os arquivos nem altere os caminhos das pastas sem atualizar as referências no código.
- A estrutura inicial não significa que as credenciais do GitHub ou a implantação na Vercel já estejam configuradas.
- Teste a loja, o painel, o carregamento das imagens e a publicação depois de configurar as integrações.

---

**MAUY** — estrutura inicial da loja virtual e do painel administrativo.
