#Requires -Version 7

[CmdletBinding()]
param(
    $InputFile = '..\input.txt'
)

# https://adventofcode.com/2022/day/7

    # a simple File class
    class File {
        [string]$name
        [int]$size
        File([string]$name,[int]$size) {
            $this.name = $name
            $this.size = $size
        }
        [string]ToString() {
            return '{0}({1})' -f $this.name,$this.size
        }
    }

    # helper that returns the parent path of a given folder
    function UpDir {
        param([string]$dir)
        $dir = $dir.Substring(0,$dir.LastIndexOf('/'))
        return ($dir -eq '') ? '/' : $dir
    }

    # parse the file structure into a hashtable where each absolute
    # folder path is a key its value is a list of file details
    $fs = @{}
    switch -Regex (Get-Content $InputFile) {

        # change directory
        '\$ cd (\S+)' {
            if ($matches[1] -eq '/') {
                $curDir = '/'
            }
            elseif ($matches[1] -eq '..') {
                $curDir = UpDir $curDir
            }
            else {
                $curDir += ($curDir -eq '/') ? $matches[1] : "/$($matches[1])"
            }

            # add the current dir to the hashtable if it doesn't exist
            if ($null -eq $fs[$curDir]) {
                $fs[$curDir] = @() -as [Collections.Generic.List[File]]
            }
        }

        # file
        '(\d+) (\S+)' {

            # add the file to the current directory
            $f = [File]::new($matches[2],$matches[1])
            $fs[$curDir].Add($f)

            # add it to all of the parent directories as well
            $tempDir = $curDir
            while ($tempDir -ne '/') {
                $tempDir = UpDir $tempDir
                $fs[$tempDir].Add($f)
            }
        }

    }

    # calculate the total size of each folder
    $folderSizes = foreach ($dir in $fs.Keys) {
        $fs[$dir]
        | Measure-Object -Sum size
        | Select-Object @{L='dir';E={$dir}},@{L='size';E={$_.Sum}}
    }

    # Part 1 Answer
    $folderSizes
    | Where-Object { $_.size -le 100000 }
    | Measure-Object -Sum size
    | Select-Object -Expand sum

    # Part 2
    $usedSpace = ($folderSizes | Where-Object { $_.dir -eq '/' }).size
    $needed = 30000000 - (70000000 - $usedSpace)
    $folderSizes
    | Where-Object { $_.size -ge $needed }
    | Sort-Object size
    | Select-Object -First 1 -Expand size