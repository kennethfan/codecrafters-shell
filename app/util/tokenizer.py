from typing import List, Optional


class Tokenizer:
    _SINGLE_QUOTE = '\''
    _DOUBLE_QUOTE = '"'
    _ESCAPE = '\\'
    _WHITE_SPACE = ' '
    _QUOTE_ESCAPE_MAPPING = {
        'a': '\a',
        'b': '\b',
        't': '\t',
        'r': '\r',
        'n': '\n',
        _ESCAPE: _ESCAPE,
        _SINGLE_QUOTE: _SINGLE_QUOTE,
        _DOUBLE_QUOTE: _DOUBLE_QUOTE,
    }

    def __init__(self, input_str: str):
        self._input_str = input_str
        self._length = len(input_str)
        self._in_single_quote = False
        self._pos = 0
        self._token_list = []
        self._cur_token_chs = []

    def tokenize(self) -> List[str]:
        while True:
            ch = self._next_ch()
            if ch is None:
                break
            self._dispatch(ch)
        self._end()
        return self._token_list

    def _dispatch(self, ch):
        if ch == self._SINGLE_QUOTE:
            self._handle_single_quote()
        elif ch == self._ESCAPE:
            self._handle_escape()
        else:
            self._handle_normal(ch)

    def _next_ch(self) -> Optional[str]:
        if self._pos < self._length:
            self._pos += 1
            return self._input_str[self._pos - 1:self._pos]
        return None

    def _end(self):
        if self._in_single_quote:
            self._error()
            return
        self._token_end()

    def _error(self):
        raise ValueError(f'{self._input_str} is valid')

    def _token_end(self):
        if len(self._cur_token_chs) == 0:
            return
        self._token_list.append(''.join(self._cur_token_chs))
        self._cur_token_chs = []

    def _handle_single_quote(self):
        # if self._in_single_quote:
        #     self._token_end()
        self._in_single_quote = not self._in_single_quote

    def _handle_escape(self):
        ch = self._next_ch()
        if ch is None:
            self._error()
            return
        if self._in_single_quote:
            mp_ch = self._QUOTE_ESCAPE_MAPPING.get(ch)
            if mp_ch is None:
                self._error()
                return
            self._cur_token_chs.append(mp_ch)
            return
        if self._WHITE_SPACE != ch:
            self._error()
            return
        self._cur_token_chs.append(self._WHITE_SPACE)

    def _handle_normal(self, ch: str):
        if ch.isspace() and not self._in_single_quote:
            self._token_end()
            return
        self._cur_token_chs.append(ch)


if '__main__' == __name__:
    test_str = """
    'adsajfld ' dajkfjdsa' 'fdsajl ' fdasfdsal fdsalf kdsa'
    """
    print(Tokenizer(test_str).tokenize())