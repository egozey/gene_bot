import requests
from bs4 import BeautifulSoup



def pars(gene,search):

    u0 = 'https://databases.lovd.nl/shared/ajax/viewlist.php?viewlistid=CustomVL_VOTunique_VOG_APC&object=Custom_ViewList&object_id=VariantOnTranscriptUnique%2CVariantOnGenome&id=APC&order=VariantOnTranscript%2FDNA%2CASC&search_transcriptid=00002660&search_VariantOnTranscript/DNA={}&page_size=100&page=1'.format(search)
    u1 = "https://databases.lovd.nl/shared/ajax/viewlist.php?viewlistid=CustomVL_VOTunique_VOG_MLH1&object=Custom_ViewList&object_id=VariantOnTranscriptUnique%2CVariantOnGenome&id=MLH1&order=VariantOnTranscript%2FDNA%2CASC&search_transcriptid=00013676&search_VariantOnTranscript/DNA={}&page_size=100&page=1".format(search)
    u2 = 'https://databases.lovd.nl/shared/ajax/viewlist.php?viewlistid=CustomVL_VOTunique_VOG_MLH3&object=Custom_ViewList&object_id=VariantOnTranscriptUnique%2CVariantOnGenome&id=MLH3&order=VariantOnTranscript%2FDNA%2CASC&search_transcriptid=00023959&search_VariantOnTranscript/DNA={}&page_size=100&page=1'.format(search)
    u3 = 'https://databases.lovd.nl/shared/ajax/viewlist.php?viewlistid=CustomVL_VOTunique_VOG_MSH2&object=Custom_ViewList&object_id=VariantOnTranscriptUnique%2CVariantOnGenome&id=MSH2&order=VariantOnTranscript%2FDNA%2CASC&search_transcriptid=00013950&search_VariantOnTranscript/DNA={}&page_size=100&page=1'.format(search)
    u4 = 'https://databases.lovd.nl/shared/ajax/viewlist.php?viewlistid=CustomVL_VOTunique_VOG_MSH6&object=Custom_ViewList&object_id=VariantOnTranscriptUnique%2CVariantOnGenome&id=MSH6&order=VariantOnTranscript%2FDNA%2CASC&search_transcriptid=00001468&search_VariantOnTranscript/DNA={}&page_size=100&page=1'.format(search)
    u5 = 'https://databases.lovd.nl/shared/ajax/viewlist.php?viewlistid=CustomVL_VOTunique_VOG_MUTYH&object=Custom_ViewList&object_id=VariantOnTranscriptUnique%2CVariantOnGenome&id=MUTYH&order=VariantOnTranscript%2FDNA%2CASC&search_transcriptid=00023838&search_VariantOnTranscript/DNA={}&page_size=100&page=1'.format(search)
    c ={'APC': [u0,12650,12,-91,-2], 'MLH1': [u1,11600,8,-91,-2],'MLH3': [u2,11600,8,-91,-2],'MSH2': [u3,11600,8,-91,-2],\
        'MSH6': [u4,11600,8,-91,-2],'MUTYH': [u5,11660,9,-91,-2]}
    response = requests.get(c[gene][0])
    soup = BeautifulSoup(response.content, "html.parser")

    text = soup.text
    check = len(text)
    flag = False
    ch = 0
    for i in text.split('\n'):

        if check < c[gene][1]:

            return text[c[gene][3]:c[gene][4]]

            break
        if i != '':
            if i.strip() == 'Owner':
                flag = True
                continue
            if i.strip() == '10 per page':
                flag = False
            if flag == True:
                ch+=1
            if ch == c[gene][2]:
                return  i
                break


