#ideaFilter

Idea filter is a utility tool. It is used for filtering out ideas/notes/data
gathrered in YAML file. Any "schema" can be used in YAML file. Filtered out
ideas are printed out in nice format based on template file.


Example usage:

```examples/interviewQuestions> ../../ideaFilter.py -i input.adoc -t template.adoc -o ../../output/interviewQuestions.txt -q '$.where($.category = JAVA)'```
