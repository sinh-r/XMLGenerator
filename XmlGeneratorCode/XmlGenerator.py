def ReadLinesToList(classPath):
    lines = []

    with open(classPath) as f:
        lines = f.readlines()

    return lines

def AddXml(lines):
    classKeyword = 'class'
    staticKeyword = 'static'
    virtualKeyword = 'virtual'
    constantKeyword = 'const'
    name = ''

    linePtr = 0
    while linePtr < len(lines):
        line = lines[linePtr].strip()
        if line.startswith('public'):
            indentations = ' ' * (len(lines[linePtr]) - len(line) - 1)
            words = lines[linePtr].split()
            if words[1] == classKeyword or words[2] == classKeyword:
                if words[1] == classKeyword:
                    name = ' '.join([words[2], classKeyword])
                else:
                    name = ' '.join([words[3], classKeyword])
            elif words[1].endswith(')') or words[2].endswith(')'):
                pass
            else:
                if words[1] in [staticKeyword, virtualKeyword, constantKeyword]:
                    name = words[3]
                else:
                    name = words[2]

            xmlComment = indentations.join([f'{indentations}///<summary>\n', f'/// {name}\n', '///</summary>\n'])
            lines.insert(linePtr, xmlComment)
            linePtr += 1
        linePtr += 1

    return lines

def WriteListToFile(classPath, lines):
    with open(classPath, 'w') as f:
        for line in lines:
            f.write(line)





classPath = 'D:/My Ideas/XMLGenerator/XmlGeneratorSample/XMLGeneratorSamples/Class1.cs'

lines = ReadLinesToList(classPath)
lines = AddXml(lines)
WriteListToFile(classPath, lines)

print('Done')