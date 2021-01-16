# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex
import ply.yacc as yacc

# List of token names.   This is always required


class MyLexer(object):
    tokens = [
        'NUMBER',
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'LPAREN',
        'RPAREN',
        'ID',
    ]

    reserved = {
        'wa': 'WA',  # and
        'b7al': 'B7AL',  # as
        'ftared': 'FTARED',  # assert
        'mamtzamench': 'MAMTZAMENCH',  # async
        'tsna': 'TSNA',  # await
        'khrej': 'KHREJ',  # break
        'naw3': 'NAW3',  # class
        'kmel': 'KMEL',  # continue
        '3aref': '3AREF',  # def
        'mse7': 'MSE7',  # del
        'wlaila': 'WLAILA',  # elif
        'wla': 'WLA',  # else
        'masd9ch': 'MASD9CH',  # except
        'khate2': 'KHATE2',  # false
        'akhiran': 'AKHIRAN',  # finally
        'lkola': 'LKOLA',  # for
        'men': 'MEN',  # from
        '3amm': '3AMM',  # global
        'ila': 'ILA',  # if
        'jib': 'JIB',  # import
        'fi': 'FI',  # in
        'huwa': 'HUWA',  # is
        'lambda': 'LAMBDA',  # lambda
        'Walo': 'WALO',  # None
        'machima7ali': 'MACHIMA7ALI',  # nonlocal
        'machi': 'machi',  # not
        'aw': 'AW',  # or
        'douz': 'DOUZ',  # pass
        'tele3': 'TELE3',  # raise
        'red': 'RED',  # return
        's7i7': 'S7I7',  # true
        'jereb': 'JEREB',  # try
        'ma7ed': 'MA7ED',  # while
        'm3a': 'M3A',  # with
        'rje3': 'RJE3',  # yield
    }

    tokens = tokens + list(reserved.values())

    # Regular expression rules for simple tokens
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'

    # literals = [ '+','-','*','/' ]

    def t_COMMENT(self, t):
        r'\#.*'

    # A regular expression rule with some action code
    def t_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value, 'ID')    # Check for reserved words
        return t

    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
    t_ignore = ' \t'

    # Error handling rule
    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Compute column.
    #     input is the input text string
    #     token is a token instance
    # def find_column(input, token):
    #     line_start = input.rfind('\n', 0, token.lexpos) + 1
    #     return (token.lexpos - line_start) + 1

    # Build the lexer
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # Test it out
    # data = '''
    # 3 + 4 * 10
    # + -20 *2
    # abc
    # if a then
    # اقرأ a then b
    # #hjh
    # input abc
    # '''

    # Give the lexer some input
    # lexer.input(data)

    # Tokenize
    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break      # No more input
            print(tok.type, tok.value, tok.lineno, tok.lexpos)
            # print(tok)
        # tok.type = token name from tokens list
        # tok.value = actual value
        # tok.lineno = line number
        # tok.lexpos = token position in line

# m = MyLexer()
# m.build()
# m.test("test \
# 3 + 4")
