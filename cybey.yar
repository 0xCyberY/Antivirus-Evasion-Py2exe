rule cybery
{
    meta:
        author = "@0xcybery"
        date = "2022-10-24"
        description = "This is a simple Yara rule to detect CyberY.exe"
        references = "https://github.com/0xCyberY/Antivirus-Evasion-Py2exe"
        filetype = "exe"

    strings:
        $a = "CyberY.pyR$"
        $b = "PYTHON27.DLL" nocase
        $c = "pythondll"
        $d = "python_typesR"
        $e = "encodings"
        $f = "getencoder"
        $g = "PY2EXE" nocase
        $h = "codecs.pyc"
        $i = "ctypes"

    condition:
        uint16(0) == 0x5a4d and all of them
}