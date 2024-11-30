if exists('g:snippets_ultisnips_loaded')
  finish
endif

let g:snippets_ultisnips_loaded = 1

inoremap / <C-R>=SnippetsUltiSnips#ExpandOrJump()<CR>
inoremap , <C-R>=SnippetsUltiSnips#CommaSnip()<CR>
