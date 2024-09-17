from Lexica import lexer
from Sintatica import parse

data = '''
cd myfolder;
ls;
pwd;
echo "Hello World";
if (x > 10) {
    echo "x is greater than 10";
} else {
    echo "x is 10 or less";
}
'''

lexer.input(data)
for token in lexer:
    print(token)

result = parse(data)
print(result)