lvim.leader = "space"

-- binds
lvim.keys.normal_mode["<leader>q"] = ":BufferKill<CR>"
lvim.keys.normal_mode["<leader>s"] = ":w<CR>"
lvim.keys.insert_mode["jk"] = "<ESC>"
lvim.keys.normal_mode["<TAB>"] = ":BufferLineCycleNext<CR>"
lvim.keys.normal_mode["<S-f>"] = ":Telescope live_grep<CR>"

-- visual
vim.o.textwidth = 0
vim.o.number = true
vim.o.wrapmargin = 0
vim.o.wrap = true
vim.o.linebreak = true
vim.o.clipboard = "unnamedplus"
vim.o.relativenumber = true

lvim.builtin.alpha.dashboard.section.header.val = {
".------..------..------..------.",
"|K.--. ||I.--. ||N.--. ||G.--. |",
"| :/\\: || (\\/) || :(): || :/\\: |",
"| :\\/: || :\\/: || ()() || :\\/: |",
"| '--'K|| '--'I|| '--'N|| '--'G|",
"`------'`------'`------'`------'",
}

-- plugins
lvim.plugins = {
  { "lunarvim/colorschemes" },
  { "Mofiqul/dracula.nvim" },
  { "loctvl842/monokai-pro.nvim" },
}

lvim.colorscheme = "monokai-pro"
