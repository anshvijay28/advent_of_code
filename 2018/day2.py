from collections import defaultdict

def solve1(ids):
    lines = ids.split("\n")
    twos, threes = 0, 0
    k = ord('a')

    for line in lines:
        if not line:
            continue
        
        counts = [0] * 26
        curr_two, curr_three = 0, 0

        for char in line:
            counts[ord(char) - k] += 1
        
        for i in range(26):
            if counts[i] == 2:
                curr_two = 1
            if counts[i] == 3:
                curr_three = 1
        
        twos += curr_two
        threes += curr_three

    return twos * threes

def solve2(ids):
    # even for a graph solution, constructing the graph is O(n^2 * m)
    # so nested for loops must be okay
    lines = ids.split("\n")
    n = len(lines)
    i = 0
    while i < n and not lines[i]: i += 1
    m = len(lines[i])

    for i in range(n):
        for j in range(i + 1, n):
            if not lines[i] or not lines[j]:
                continue
                
            # compare
            diffs = 0
            idx = 0

            for k in range(m):
                if lines[i][k] != lines[j][k]:
                    diffs += 1
                    idx = k
            
            if diffs == 1:
                # missing edge case when idx = m - 1, but idc 
                return lines[i][:idx] + lines[i][idx+1:]

ids = """
evsialkqydurohxqpwbcugtjmh
evsialkqydurohxzssbcngtjmv
fvlialkqydurohxzpwbcngujmf
nvsialkqydorohxzpwpcngtjmf
evsialjqydnrohxypwbcngtjmf
vvsialyqxdurohxzpwbcngtjmf
yvsialksydurowxzpwbcngtjmf
evsillkqydurbhxzpmbcngtjmf
ivsialkqyxurshxzpwbcngtjmf
ejsiagkqyduhohxzpwbcngtjmf
evsialkqldurohxzpcbcngtjmi
evsialkqydurohxzpsbyngtkmf
ersialkeydurohxzpwbcngtpmf
evsialuqzdkrohxzpwbcngtjmf
evswulkpydurohxzpwbcngtjmf
evsialkqyiurohxzpwucngttmf
evtialkqydurphxzywbcngtjmf
evsialkzyiurohxzpwbcxgtjmf
evsiaykqydurohxzpwbcggtjuf
evxqalkqydurohmzpwbcngtjmf
eisralkqydurohxzpdbcngtjmf
evsfalkqydurohxzpwbangtjwf
evbialkqydurohxzawbcngtjmg
evsialkqydrrohxrpcbcngtjmf
evsialkqycurohxzpvbcngtjkf
evsialkqsdudohxzpwbcnotjmf
evsiackqydurohxzpmbsngtjmf
evsialmqykurohxzpwbfngtjmf
evsialsqydurohxzpwucngtjxf
tvsialkqyeurohxzpwbcrgtjmf
zvsialkqydbrohxzpwbcnltjmf
evsmbskqydurohxzpwbcngtjmf
evsialkqydurohxzpwbcngpgmt
evsialkqydurlyezpwbcngtjmf
evoialkqyturohxzpwbcnjtjmf
evsialkqydurohxspkfcngtjmf
evsiaikqydurohxjpwbcngtjmd
evsialkyydurohxzvwbcngtjmc
svsialkqyduhohxzpwbhngtjmf
eysillkqydurohxzhwbcngtjmf
evsialkqyduetaxzpwbcngtjmf
evsialkqxdurshxzpwbcngtjmb
evsiadkqydwrovxzpwbcngtjmf
evsialkqydurokxzpwbcngjjef
evskalkqymurohxzpybcngtjmf
cvsialkqydurohxzpwbcnbtjma
evsialkqydurohxzawhcngtjuf
evsiahkqfduroixzpwbcngtjmf
evsivlkqyduroqxzpwbctgtjmf
evsiarkqyduroixzywbcngtjmf
evspalkqydurohxzpwlcngxjmf
eesialkqydurohxzpalcngtjmf
gvsualkqydurohxzpwbmngtjmf
evsialkqydurlhxzpwbcngsjmq
evsialhqydfrohxopwbcngtjmf
evzialkqydsrohxzpwbcngtjmw
evbpalkqydurbhxzpwbcngtjmf
mvsialkqydurohxzpwbcnghjmr
evsialkqsdurohxzpkbcngtjxf
ejkialktydurohxzpwbcngtjmf
evsialkqyauoohxzpwbqngtjmf
evsiklkyyduroqxzpwbcngtjmf
evgialkqydurohxzpwocngthmf
ebsialkqydcrohxzpwbcngtbmf
evsialkqysurohxzpwfingtjmf
evsialkqddurmhxzpwbnngtjmf
evsialkqydurohxoiwwcngtjmf
evsialkqydurohpzkzbcngtjmf
vvsealkqydurorxzpwbcngtjmf
evsialkqyduroqxzpwlungtjmf
eviialkqiyurohxzpwbcngtjmf
evzsalkqyaurohxzpwbcngtjmf
exsialkqydurohfzpwbwngtjmf
evsialkqyduruhxkpwbcnytjmf
essiatkqydurohxzpwbxngtjmf
evsialkqyduroamzpwbcngtjcf
wvsialkqyduruhxzpwbcnxtjmf
evsialkqydurohxgpwbcngtjeh
evsialfqxdurohxzpwbcngtomf
evsialkqyourghxzpwbcngtbmf
evsoaokqydurohxzpwbcngtamf
evsialpqydurohxzpwccxgtjmf
evsialkqzdurxhxgpwbcngtjmf
ezsialkqmdurohxzpwbcngtjmi
cvsialjeydurohxzpwbcngtjmf
evsialkqydurocxupwbcvgtjmf
evscalkqydtrohxzpebcngtjmf
evjialkqyduiohxzpabcngtjmf
evsialjqyduruhxzppbcngtjmf
evsialkqydurfhxzpwbcuqtjmf
evsialkqyiurohizpwucngttmf
evsialiqydurrhxzpwbcngdjmf
evbialkqywurohxzpwhcngtjmf
evsialkqyduloyxzpwbqngtjmf
evsialxqyduzohxzpwbqngtjmf
vvsialkqydurohxzpwbcnqpjmf
evsialksydurohxzcwbmngtjmf
pvsialkqydurohxzpwucngtjvf
evsialkqydurohmkpwbcngtfmf
mvsialkqydurphyzpwbcngtjmf
evsialkqydyrohxzhwbcnitjmf
evsialokydurozxzpwbcngtjmf
evsialkqyduroexfcwbcngtjmf
evsiavkqydurohxzpwbcnmtjme
evsiawkqydurohxzpwbcngojjf
evsialkaydurohxzpwfcngtjff
evsialkaydurohxzpwbcngtjpb
gvsialkqyburorxzpwbcngtjmf
evszalkqydurphxzpwocngtjmf
evsualkqyduropxzpwbcngejmf
evsitlkqydurshxzpwbcngtkmf
evbixlkqydrrohxzpwbcngtjmf
elsialkqydprohxzpwbcngtrmf
evsialkqydurohbzpwbcggtjmc
evtoalqqydurohxzpwbcngtjmf
evsralhqydurohxzowbcngtjmf
evsialkhydurohxzlsbcngtjmf
evsialkqydurohxvpwbcnuujmf
evsialkqydurocxzuwbcngtjmi
evsialkqndyrokxzpwbcngtjmf
evsialkqydurywfzpwbcngtjmf
evsialkqydurohxzwwbcngthms
eqsiahkqydurohxzpwbyngtjmf
evsdalkqydurohxzpwbcnjkjmf
evsialkqyddrohplpwbcngtjmf
evshalkqydurohxzpfxcngtjmf
evvialkqydurohxapwbcngtjmh
evsialkqyduvohxzpwbcnnvjmf
evsiblkqedurohxzpwbkngtjmf
evsvalkqfdutohxzpwbcngtjmf
evsialjqydurohxzpwbcnctjsf
evsialkxywurohxdpwbcngtjmf
evsiagkqydurohxzpwzcjgtjmf
ebsialkqydurohxzpxfcngtjmf
evsialkqysfrohxzpwbcngtjlf
evvialkqyqurwhxzpwbcngtjmf
evxialkqydurohxzpwgcnrtjmf
vvsillkqydurohxzpwbcvgtjmf
evsiwlkqyduoohxzpwbcngtjxf
evsialkqypurohezpwbcngtjwf
evbialkqydurohxipwbcnftjmf
evsiakkqyduyohxzpwbcngtjmu
evsialkqydurohzzpwxqngtjmf
evsialkqykurkhxzpwocngtjmf
dvriplkqydurohxzpwbcngtjmf
evsialkqgdurohxzpwbmnctjmf
evsialkqyuurohxzpwtcngtjmj
wvsialkqydurohxzpwbchgejmf
eusimlsqydurohxzpwbcngtjmf
evsialkqydqrohxzhwbcngtjmh
wvswalkqydurohxzpwbcngjjmf
evsialkqyourohxzkwbcngttmf
evaialkqydurohxzbubcngtjmf
evfialkqydueohxzpwbclgtjmf
evrialkqydurohxzpwbcnctjmh
evsiaojqydxrohxzpwbcngtjmf
evsualkqywuxohxzpwbcngtjmf
evsialkdydrzohxzpwbcngtjmf
evlialkqyfurohxzpwbcnotjmf
epsialkqydujohxzpwbcngtjif
evsialkqyaucohxgpwbcngtjmf
lvsialaqydurohxzpwbcngtjzf
evsialkgydurohezpwbcngtjmo
lvsialkqydurosxwpwbcngtjmf
evsiaekqyqurohxzpvbcngtjmf
evsiapkqydirohxzpwbzngtjmf
zvsixlkwydurohxzpwbcngtjmf
evaialkqyduoohxzpwbcngtjkf
evsialcqedurohxzpwbcngtjmc
evjialkgydurohxzpwbwngtjmf
evsialkqcdurohxzpwbcpgojmf
evsialkqkdurohxzlwbcngtrmf
eosiylkzydurohxzpwbcngtjmf
evsialkqydurohhzpwscnmtjmf
evsiallqydurobxzpwbxngtjmf
evsialkqydurohwztwhcngtjmf
evsiallqydurohxzpwbcygjjmf
evsiabkqywurohxzpwbcngtjmy
evsiackqydzrohxznwbcngtjmf
evsiazkqzdurooxzpwbcngtjmf
evsialcqydurghxzpwbcngtjmc
yvsiaxkqydurohxzpwbcxgtjmf
evsiylkqgdhrohxzpwbcngtjmf
lvsialkqydurohxgcwbcngtjmf
evsiglkqydurohxzpwbvngzjmf
evsialkqyvurohxzpwbcngtjnz
evsialkgydueohxzpwbcpgtjmf
cvsiavkqyddrohxzpwbcngtjmf
evsialklyrurohxzpwbcngtjff
eisialkqyduwohxzpwbcngcjmf
evsialkqydrrihwzpwbcngtjmf
easialkqydurohxzpwbcnltrmf
evsialfqydurohxzpybcnytjmf
eqsialkqycurohxzywbcngtjmf
evsitlkqmdurohxzpwbcngtjmx
evsiclsqyduroixzpwbcngtjmf
elsialrqydurohxzpwmcngtjmf
evsiapkqodurohxzpwbcogtjmf
evstalkeydurohxzpibcngtjmf
evsihlkqyqurohxzpwblngtjmf
euszalkqydurohxipwbcngtjmf
ezsialksydurohxzpwbcngfjmf
eisialkdydurohxzpwbcngtumf
evsirlkaydprohxzpwbcngtjmf
evsiklkqydnrohxzpwbcngtjmu
evsialkqydnuohxzpwbcngtjmu
eksialkqydurohxztwfcngtjmf
evlialkqedurohxzpwbhngtjmf
evqialkqydurohxzpubcngtjpf
evsialkwydurohwzpwbcnmtjmf
evsiaokqcdurohxzpwbcngtjcf
evsialkkyfurohxzpvbcngtjmf
evsialkqyduromxzpwqcngtimf
evsialkqydumohxzpwbcnmtjsf
evsialddydurehxzpwbcngtjmf
evsialkqydurohxzpobcnptjmk
evsiagkqydurohhzpwbcxgtjmf
evsfalkqydurohszpwbangtjmf
evgialkzyduqohxzpwbcngtjmf
evaialkqzdurohxzpwbcngtjmo
evsialkqyqurohxjpwbcnntjmf
evsialkjydybohxzpwbcngtjmf
evskalgqydurohxzrwbcngtjmf
evsialkqydurohxzpjbcymtjmf
evsialkqqdurohxzpybcngtjyf
evsialkqydqrbhxzpwbcngtjmj
evssalaqrdurohxzpwbcngtjmf
mvsialkfydurohxzpwbcngtjmk
evsialkqwdurohxzpwgcngtjdf
evqkalkqydurohxzpwbcngajmf
evbialkqydurohxzpibcngejmf
evszalkqydurbhxzpwbcngtjsf
evsialkqydurohxepwbcngtjjo
evsialkqcdubmhxzpwbcngtjmf
evsiarkqyduroaxzpwbcngtjmp
evsiakkqyduzohczpwbcngtjmf
evtualkqydurofxzpwbcngtjmf
ejsialkqvdurohzzpwbcngtjmf
evsialkqydurohczpwbcngqvmf
svsianfqydurohxzpwbcngtjmf
evsialiqydurohxzpwbcngzqmf
ejsialhqydurohxzpwjcngtjmf
evpialkqydurohxzpwbcnbtjff
evsialkuyvurohxzpwbcngtjkf
eqsialkqydurohxzpwbcnwtcmf
evsiatkqydkrohxzpwkcngtjmf
evsialkqydurohxzpebciytjmf
evsialkqydrrohxzpwtcngtfmf
evsialkqjducohxzpwycngtjmf
evsialkqydurohxzpwicnxtjnf
"""

print(solve2(ids))
