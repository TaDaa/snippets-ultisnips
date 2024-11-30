let s:py_cmd = 0
if has('python3')
  let s:py_cmd = "py3"
elseif has('python')
  let s:py_cmd = "py"
endif

let g:snippets_ultisnips_current_directory = resolve(expand('<sfile>:p:h').'/../lib')
let g:snippets_ultisnips_check_move_result = 0
let g:snippets_ultisnips_skip_return = 0

if s:py_cmd =~ "py"
  exec s:py_cmd join([
  \ "import vim",
  \ "sys.path.append(vim.eval('g:snippets_ultisnips_current_directory'))",
  \ ], "\n")
endif

function SnippetsUltiSnips#ExpandOrJump()
  exec s:py_cmd  "import SnippetsUltiSnips; SnippetsUltiSnips.check_move()"
  if g:snippets_ultisnips_skip_return == 0
    return g:snippets_ultisnips_check_move_result
  endif
  return ''
endfunction

function! SnippetsUltiSnips#CommaSnip()
    exec s:py_cmd "import SnippetsUltiSnips; SnippetsUltiSnips.check_comma()"
    if g:tadaa_regex_res
        return '/'
    endif
    return ','
endfunction
