with import <nixpkgs> {};

stdenv.mkDerivation {
  name = "env";

  buildInputs = [
    python3
  ] ++ (with python36Packages; [
    fonttools
  ]);
}

