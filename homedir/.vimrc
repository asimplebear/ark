"highlight trailing whitespace
highlight RedundantSpaces ctermbg=red guibg=red
match RedundantSpaces /\s\+$/

"remove trailing whitespace on write
"autocmd BufWritePre * :%s/\s\+$//



"show tab as !------
set list
set listchars=tab:!-
