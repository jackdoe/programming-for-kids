package main

import (
	"encoding/json"
	"encoding/xml"
	"os"
)

type LexicalResource struct {
	XMLName           xml.Name `xml:"LexicalResource"`
	Text              string   `xml:",chardata"`
	GlobalInformation struct {
		Text  string `xml:",chardata"`
		Label string `xml:"label,attr"`
	} `xml:"GlobalInformation"`
	Lexicon struct {
		Text           string `xml:",chardata"`
		LanguageCoding string `xml:"languageCoding,attr"`
		Label          string `xml:"label,attr"`
		Language       string `xml:"language,attr"`
		Owner          string `xml:"owner,attr"`
		LexicalEntry   []struct {
			Text         string `xml:",chardata"`
			ID           string `xml:"id,attr"`
			PartOfSpeech string `xml:"partOfSpeech,attr"`
			Lemma        struct {
				Text        string `xml:",chardata"`
				WrittenForm string `xml:"writtenForm,attr"`
			} `xml:"Lemma"`
			WordForms struct {
				Text     string `xml:",chardata"`
				WordForm []struct {
					Text              string `xml:",chardata"`
					WrittenForm       string `xml:"writtenForm,attr"`
					GrammaticalNumber string `xml:"grammaticalNumber,attr"`
					Article           string `xml:"article,attr"`
				} `xml:"WordForm"`
			} `xml:"WordForms"`
			Morphology struct {
				Text       string `xml:",chardata"`
				MorphoType string `xml:"morphoType,attr"`
			} `xml:"Morphology"`
			MorphoSyntax struct {
				Text                           string `xml:",chardata"`
				PronominalAndGrammaticalGender string `xml:"pronominalAndGrammaticalGender,attr"`
			} `xml:"MorphoSyntax"`
			Sense struct {
				Text           string `xml:",chardata"`
				ID             string `xml:"id,attr"`
				SenseId        string `xml:"senseId,attr"`
				Definition     string `xml:"definition,attr"`
				Synset         string `xml:"synset,attr"`
				Provenance     string `xml:"provenance,attr"`
				Annotator      string `xml:"annotator,attr"`
				SenseRelations string `xml:"SenseRelations"`
				SemanticsNoun  struct {
					Text         string `xml:",chardata"`
					Reference    string `xml:"reference,attr"`
					Countability string `xml:"countability,attr"`
					SemanticType string `xml:"semanticType,attr"`
				} `xml:"Semantics-noun"`
				Pragmatics    string `xml:"Pragmatics"`
				SenseExamples []struct {
					Text         string `xml:",chardata"`
					SenseExample struct {
						Text          string `xml:",chardata"`
						ID            string `xml:"id,attr"`
						CanonicalForm struct {
							Text           string `xml:",chardata"`
							Canonicalform  string `xml:"canonicalform,attr"`
							ExpressionType string `xml:"expressionType,attr"`
						} `xml:"canonicalForm"`
						SyntaxEx struct {
							Text      string `xml:",chardata"`
							CombiWord []struct {
								Text         string `xml:",chardata"`
								Lemma        string `xml:"lemma,attr"`
								PartOfSpeech string `xml:"partOfSpeech,attr"`
							} `xml:"combiWord"`
						} `xml:"Syntax_ex"`
						SemanticsEx string `xml:"Semantics_ex"`
						Pragmatics  string `xml:"Pragmatics"`
					} `xml:"SenseExample"`
				} `xml:"SenseExamples"`
			} `xml:"Sense"`
		} `xml:"LexicalEntry"`
	} `xml:"Lexicon"`
}

type SimpleWord struct {
	Word       string   `json:"word"`
	Definition string   `json:"definition"`
	Examples   []string `json:"examples,omitempty"`
}

func main() {
	dec := xml.NewDecoder(os.Stdin)
	data := &LexicalResource{}
	err := dec.Decode(data)
	if err != nil {
		panic(err)
	}

	out := []*SimpleWord{}

	for _, row := range data.Lexicon.LexicalEntry {
		simple := &SimpleWord{
			Word:       row.Lemma.WrittenForm,
			Definition: row.Sense.Definition,
		}
		if simple.Definition == "" || simple.Word == "" {
			continue
		}
		for _, example := range row.Sense.SenseExamples {
			if example.SenseExample.CanonicalForm.Canonicalform != "" {
				simple.Examples = append(simple.Examples, example.SenseExample.CanonicalForm.Canonicalform)
			}
		}
		out = append(out, simple)
	}
	j := json.NewEncoder(os.Stdout)
	j.SetIndent("", "  ")
	err = j.Encode(out)
	if err != nil {
		panic(err)
	}
}
