SKEM_REPO="https://github.com/AT-WORLDS-END/Yamlok-userbot-Extra.git"
FOLDER="./ExtraPlugins"
reqirements_file="./ExtraPlugins/Extrarequirements.txt"

make_dir () {
  if [[ -d "$FOLDER" ]] 
  then
    rm -r "$FOLDER"
    mkdir "$FOLDER"
  else
    mkdir "$FOLDER"
  fi
}


git_clone () {
  git clone "$SKEM_REPO" "$FOLDER"
}

req_installer () {
    pip3 install --no-cache-dir -r "$reqirements_file"
}

fetch_plugins () {
  make_dir
  git_clone
  req_installer
}

fetch_plugins
