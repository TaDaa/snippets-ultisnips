# import sys
# PY_CMD = "py"
# if (sys.version_info > (3, 0)):
    # PY_CMD = "py3"

import vim
import os
from UltiSnips import UltiSnips_Manager

is_win = vim.eval('has("win32")') == "1"

def hook(row,col):
    snippet = None
    start_cursor = vim.current.window.cursor
    ln = len(UltiSnips_Manager._active_snippets)
    last = None
    while ln >= 1 and UltiSnips_Manager._active_snippets[ln - 1] != snippet:
        snippet = UltiSnips_Manager._active_snippets[ln - 1]
        cursor = vim.current.window.cursor
        if last == None:
            last = snippet
        UltiSnips_Manager.jump_forwards()
        ln = len(UltiSnips_Manager._active_snippets)
        if ln > 0:
            end = snippet.end
            if cursor[0] == end[0] + 1 and cursor[1] == end[1] and UltiSnips_Manager._active_snippets[ln - 1] != snippet and last.end[0] == snippet.end[0] and last.end[1] == snippet.end[1]:
                last = snippet
                continue
            else:
                break
        else:
            break
    if start_cursor[0] > vim.current.window.cursor[0] or (start_cursor[0] == vim.current.window.cursor[0] and start_cursor[1] > vim.current.window.cursor[1]):
        vim.current.window.cursor = (start_cursor[0],start_cursor[1])
    return ''

def check_move():
    import re
    vim.command('set eventignore=all')

    UltiSnips_Manager._cursor_moved()
    cursor = vim.current.window.cursor
    col = cursor[1]-1
    row = cursor[0]-1
    line = vim.current.buffer[row][col:]
    if len(line) != 0 and line[0] != ' ':
        UltiSnips_Manager.expand()
    else:
        vim.vars['ulti_expand_res'] = 0

    if int(vim.vars['ulti_expand_res']) != 0:
        vim.vars['snippets_ultisnips_check_move_result'] = ''
    else:
        if len(line) == 0 or line[0] == ' ' and vim.vars['snippets_ultisnips_check_move_result'] == ' ':
            if len(line):
                # echo 1
                # for YCM
                # vim.vars['snippets_ultisnips_check_move_result']=" "
                # vim.eval('feedkeys("\<bs>\<bs>\<C-R>='+PY_CMD+'eval(\'hook('+str(row)+','+str(col)+')\')\<CR>")')
                # if 'ycm_auto_trigger' in vim.vars and vim.vars['ycm_auto_trigger']:
                # if int(vim.eval("pumvisible()")):
                    # vim.vars['snippets_ultisnips_check_move_result']=" "
                    # vim.eval('feedkeys("\<bs>\<bs>\<C-R>='+PY_CMD+'eval(\'hook('+str(row)+','+str(col)+')\')\<CR>")')
                # else:
                    # vim.eval('feedkeys("\<bs>")')
                    # vim.vars['snippets_ultisnips_check_move_result']="\<bs>"
                # cursor = vim.current.window.cursor
                if is_win:
                    vim.current.buffer[row] = vim.current.buffer[row][0:col] + vim.current.buffer[row][col+1:]
                else:
                    vim.current.buffer[row] = vim.current.buffer[row][0:col] + vim.current.buffer[row][col+1:]
                UltiSnips_Manager._cursor_moved()
                hook(row,col)
                vim.vars['snippets_ultisnips_check_move_result'] = ''
            else:
                UltiSnips_Manager.expand_or_jump()
                vim.vars['snippets_ultisnips_check_move_result'] = ''
        else:
            if vim.current.buffer[row][col] != ' ':
                if is_win:
                    # vim.current.window.cursor = (row+1,col+1)
                    # vim.eval('feedkeys(" ", "nt")')
                    # vim.vars['snippets_ultisnips_check_move_result']=" "
                    # vim.vars['snippets_ultisnips_skip_return'] = 1
                    vim.eval('feedkeys("'+vim.current.buffer[row][col]+'", "nt")')
                    vim.eval('feedkeys(" ", "nt")')
                    UltiSnips_Manager._cursor_moved()
                    vim.vars['snippets_ultisnips_check_move_result']=" "
                else:
                    vim.eval('feedkeys("'+vim.current.buffer[row][col]+'", "nt")')
                    vim.eval('feedkeys(" ", "nt")')
                    UltiSnips_Manager._cursor_moved()
                    vim.vars['snippets_ultisnips_check_move_result']=" "

                UltiSnips_Manager._cursor_moved()
            else:
                UltiSnips_Manager.expand_or_jump()
                vim.vars['snippets_ultisnips_check_move_result'] = ''
    vim.command('set eventignore=')

def check_comma():
    cursor = vim.current.window.cursor
    col = cursor[1]-1
    row = cursor[0]-1
    buffer = vim.current.window.buffer[row]
    if len(buffer) > 0 and buffer[col] == ',':
        vim.current.window.buffer[row]=buffer[:col] + buffer[col+1:]
        vim.current.window.cursor = (row+1,col)
        vim.vars['tadaa_regex_res']=1
    else:
        vim.vars['tadaa_regex_res']=0
