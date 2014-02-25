#!/bin/sh
echo "==> Installing zsh"

mkdir -p ~/.zsh

rm -r ~/.zsh/zshuery
cp -r zshuery ~/.zsh/zshuery

rm -r ~/.zsh/zsh-hl
cp -r zsh-hl ~/.zsh/zsh-hl

rm -r ~/.zsh/zsh-hss
cp -r zsh-hss ~/.zsh/zsh-hss

rm ~/.zshrc
cp zshrc ~/.zshrc

echo "==> Installed zsh"
