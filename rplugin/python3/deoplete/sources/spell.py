from .base import Base


class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'spell'
        self.mark = '[spell]'
        self.rank = 50
        self.is_volatile = True

    def gather_candidates(self, ctx):
        return self.vim.funcs.spellsuggest(ctx['complete_str'])
