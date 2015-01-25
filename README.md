amherst-datamatch
=================
1. user accesses our website (hosted somewhere)
2. user signs in using amherst credentials (authentication)
3. user is redirected to form
4. user enters amherst username/email, class year, phone number (optional), WHO THEY ARE AND WHO THEY'RE SEEKING
  * need to account for a multitude of gender identities
  * I identify as a....(woman) (man) (non-binary) //exclusive
  * Seeking someone who identifies as a (woman) (man) (nonbinary) //non-exclusive
  * information stored in mongo using username as key
5. user fills out form  
  * 10 multiple-choice questions
  * include buzzfeed-like pictures
6. user clicks submit
  * answers are stored in mongo under username (key)

...VALENTINE'S DAY
1. user receives an email with their top 3 matches: name, year, email, phone number?, plus a cute picture of a baby animal
  * algorithm analyzes responses to determine most answers in common, returns top 3 keys
  * automated sent email from some account (create new one just for this?)
  
technologies: flask, python, mongo, frontend (html+css), email account to send results, someplace to host the web app, authentication technology
