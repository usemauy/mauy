# Arquivos editáveis da loja cliente

A pasta `cliente/` contém o site público da MAUY. A logo exibida no cabeçalho e no rodapé é `imglogo.svg`, e o ícone/fav icon é `imgicone.svg`.

## Editar a logo

- Abra `imglogo.svg` em um editor vetorial como Figma, Inkscape ou Illustrator para alterar formas e cores mantendo a qualidade em qualquer tamanho.
- A versão atual usa os vetores originais fornecidos para MAUY Fitness: vinho `#59283B` e nude `#C5A99A`.
- Para trocar por outra logo, substitua o conteúdo do arquivo `cliente/imglogo.svg`, preservando esse nome para que o site continue exibindo a imagem automaticamente.

## Editar o ícone

- `imgicone.svg` é o ícone vetorial MAUY usado como favicon pelo cliente.
- Substitua o conteúdo de `cliente/imgicone.svg` para personalizá-lo; mantenha o nome para conservar o vínculo.

## Conteúdo da loja

Os produtos e suas imagens são configurados pelo painel em `../admin/` e nos arquivos `produtos.json` e `site.json` na raiz do repositório. As alterações salvas no navegador do painel precisam ser exportadas e publicadas para aparecer para todos os clientes.
