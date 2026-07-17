-- Neovim config: native LSP with clangd for C/C++ (nvim 0.12+)

-- Themes (installed automatically on first launch via built-in vim.pack)
vim.pack.add({
  'https://github.com/folke/tokyonight.nvim',
  'https://github.com/catppuccin/nvim',
  'https://github.com/ellisonleao/gruvbox.nvim',
  'https://github.com/rebelot/kanagawa.nvim',
})
vim.cmd.colorscheme('tokyonight-night')

-- General options
vim.o.number = true
vim.o.relativenumber = true
vim.o.tabstop = 4
vim.o.shiftwidth = 4
--vim.o.expandtab = true
vim.o.smartindent = true
vim.o.termguicolors = true
vim.o.signcolumn = 'yes'
vim.o.updatetime = 300
vim.o.completeopt = 'menuone,noselect,popup'
vim.o.mouse = 'a'
-- Lua language server (configured for Neovim config editing)
vim.lsp.config('lua_ls', {
  cmd = { 'lua-language-server' },
  filetypes = { 'lua' },
  root_markers = { '.luarc.json', '.git' },
  settings = {
    Lua = {
      runtime = { version = 'LuaJIT' },       -- Neovim embeds LuaJIT, not standard Lua
      workspace = {
        library = vim.api.nvim_get_runtime_file('', true),  -- teach it Neovim's runtime files
      },
      diagnostics = {
        globals = { 'vim' },                   -- stop "undefined global 'vim'" warnings
      },
    },
  },
})
vim.lsp.enable('lua_ls')
-- TypeScript / JavaScript language server
vim.lsp.config('ts_ls', {
  cmd = { 'typescript-language-server', '--stdio' },
  filetypes = { 'javascript', 'javascriptreact', 'typescript', 'typescriptreact' },
  root_markers = { 'tsconfig.json', 'package.json', '.git' },
})
vim.lsp.enable('ts_ls')
-- clangd: C/C++ language server
vim.lsp.config('clangd', {
  cmd = {
    'clangd',
    '--background-index',
    '--clang-tidy',
    '--header-insertion=iwyu',
    '--completion-style=detailed',
  },
  filetypes = { 'c', 'cpp', 'objc', 'objcpp', 'cuda' },
  root_markers = { '.clangd', 'compile_commands.json', 'compile_flags.txt', '.git' },
})
vim.lsp.enable('clangd')

-- Diagnostics display
vim.diagnostic.config({
  virtual_text = true,
  severity_sort = true,
  float = { border = 'rounded' },
})

vim.api.nvim_create_autocmd('LspAttach', {
  callback = function(args)
    local client = assert(vim.lsp.get_client_by_id(args.data.client_id))

    -- Autocompletion as you type (accept with <C-y>)
    if client:supports_method('textDocument/completion') then
      vim.lsp.completion.enable(true, client.id, args.buf, { autotrigger = true })
    end

    local opts = { buffer = args.buf }
    vim.keymap.set('n', 'gd', vim.lsp.buf.definition, opts)
    vim.keymap.set('n', 'gD', vim.lsp.buf.declaration, opts)
    vim.keymap.set('n', '<leader>f', function() vim.lsp.buf.format({ async = true }) end, opts)
    vim.keymap.set('n', '<leader>e', vim.diagnostic.open_float, opts)

    -- clangd extension: jump between header and source with <leader>h
    if client.name == 'clangd' then
      vim.keymap.set('n', '<leader>h', function()
        client:request('textDocument/switchSourceHeader',
          { uri = vim.uri_from_bufnr(args.buf) },
          function(err, result)
            if err or not result then
              vim.notify('No corresponding header/source file found', vim.log.levels.WARN)
              return
            end
            vim.cmd.edit(vim.uri_to_fname(result))
          end, args.buf)
      end, opts)
    end
  end,
})

-- Keybinds
-- F5: compile & run current C++ file
vim.keymap.set('n', '<F8>', function()
  vim.cmd('write')
  local src = vim.fn.expand('%')
  local src_input = vim.fn.expand('%:r') .. '.in.txt'
  local exe = vim.fn.expand('%:r') .. '.exe'
  vim.cmd('split | terminal g++ -std=c++20 -O2 -Wall "' .. src .. '" -o "' .. exe .. '" && "' .. exe .. '" < "'.. src_input ..'"')
end)

vim.keymap.set('n', '<F9>', function() 
	local lines = vim.api.nvim_buf_get_lines(0 , 0, -1, false)
	local lines_as_string = table.concat(lines, '\n')
	vim.fn.setreg("+", lines_as_string);

end)
