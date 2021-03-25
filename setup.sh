mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"mateus.guimaraes048@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS = false \n\
port = $PORT\n\

[theme]\n\
primaryColor=\"#e6e326\"\n\
backgroundColor=\"#474748\"\n\
secondaryBackgroundColor=\"#18191a\"\n\
textColor=\"#fafafa\"\n\
font=\"serif\"\n\
" >/.streamlit/config.toml

