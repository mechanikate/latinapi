from endingdb import *
import sys
def retrieve_verb(stems, conjugation, conjugation_variant, voice="*", mood="*", case="*", number="*", person="*"):
    stem_index, ending = database["verb"][str(conjugation)+str(conjugation_variant)][voice][mood][case][number][str(person)]
    warning_flag = stems[stem_index] == "NO_STEM"
    stem = stems[0]+"t" if warning_flag else stems[stem_index]
    return (stem+ending, warning_flag)

def retrieve_noun(stems, declension, declension_variant, number, case):
    stem_index, ending = database["noun"][str(declension)+str(declension_variant)][number][case]
    return (stems[stem_index]+ending, False)
