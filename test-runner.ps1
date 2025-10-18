#Requires -Version 5.1

<#
.SYNOPSIS
    Test runner for 5 coding questions.

.DESCRIPTION
    This PowerShell script runs all 5 coding questions and reports the results.
    It checks if Python is installed, runs each question's solution, and 
    provides a summary of all tests.

.EXAMPLE
    .\test-runner.ps1
    Runs all 5 coding questions and displays results.

.NOTES
    Author: Automated Test Runner
    Requires: Python 3.x
#>

# Color output functions
function Write-Success {
    param([string]$Message)
    Write-Host $Message -ForegroundColor Green
}

function Write-Failure {
    param([string]$Message)
    Write-Host $Message -ForegroundColor Red
}

function Write-Info {
    param([string]$Message)
    Write-Host $Message -ForegroundColor Cyan
}

function Write-Header {
    param([string]$Message)
    Write-Host ""
    Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Yellow
    Write-Host $Message -ForegroundColor Yellow
    Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Yellow
}

# Check if Python is installed
function Test-PythonInstalled {
    try {
        $pythonVersion = python --version 2>&1
        if ($LASTEXITCODE -eq 0) {
            Write-Success "✓ Python is installed: $pythonVersion"
            return $true
        }
    }
    catch {
        Write-Failure "✗ Python is not installed or not in PATH"
        Write-Info "Please install Python 3.x from https://www.python.org/"
        return $false
    }
    return $false
}

# Run a single coding question
function Test-CodingQuestion {
    param(
        [int]$QuestionNumber,
        [string]$QuestionPath,
        [string]$Description
    )
    
    Write-Header "Question $QuestionNumber : $Description"
    
    $scriptPath = Join-Path $QuestionPath "solution.py"
    
    if (-not (Test-Path $scriptPath)) {
        Write-Failure "✗ Solution file not found: $scriptPath"
        return $false
    }
    
    try {
        # Run the Python script
        $output = python $scriptPath 2>&1
        $exitCode = $LASTEXITCODE
        
        # Display the output
        Write-Host $output
        
        if ($exitCode -eq 0) {
            Write-Success "✓ Question $QuestionNumber - All tests passed!"
            return $true
        }
        else {
            Write-Failure "✗ Question $QuestionNumber - Some tests failed!"
            return $false
        }
    }
    catch {
        Write-Failure "✗ Error running Question $QuestionNumber : $_"
        return $false
    }
}

# Main execution
function Main {
    # Print banner
    Write-Host ""
    Write-Host "╔═══════════════════════════════════════════════════════════╗" -ForegroundColor Magenta
    Write-Host "║         CODING QUESTIONS TEST RUNNER                     ║" -ForegroundColor Magenta
    Write-Host "║         Testing 5 Coding Questions                       ║" -ForegroundColor Magenta
    Write-Host "╚═══════════════════════════════════════════════════════════╝" -ForegroundColor Magenta
    Write-Host ""
    
    # Check Python installation
    if (-not (Test-PythonInstalled)) {
        Write-Host ""
        Write-Failure "Cannot proceed without Python. Please install Python and try again."
        exit 1
    }
    
    Write-Host ""
    
    # Define all coding questions
    $questions = @(
        @{
            Number = 1
            Path = "question1"
            Description = "Palindrome Checker"
        },
        @{
            Number = 2
            Path = "question2"
            Description = "FizzBuzz"
        },
        @{
            Number = 3
            Path = "question3"
            Description = "Array Sum"
        },
        @{
            Number = 4
            Path = "question4"
            Description = "Find Duplicates"
        },
        @{
            Number = 5
            Path = "question5"
            Description = "String Reversal"
        }
    )
    
    # Run all questions and track results
    $results = @()
    
    foreach ($question in $questions) {
        $passed = Test-CodingQuestion -QuestionNumber $question.Number `
                                      -QuestionPath $question.Path `
                                      -Description $question.Description
        
        $results += @{
            Number = $question.Number
            Description = $question.Description
            Passed = $passed
        }
        
        Start-Sleep -Milliseconds 500
    }
    
    # Print summary
    Write-Header "TEST SUMMARY"
    
    $passedCount = 0
    $totalCount = $results.Count
    
    foreach ($result in $results) {
        $status = if ($result.Passed) { "✓ PASS" } else { "✗ FAIL" }
        $color = if ($result.Passed) { "Green" } else { "Red" }
        
        Write-Host "Question $($result.Number) - $($result.Description): " -NoNewline
        Write-Host $status -ForegroundColor $color
        
        if ($result.Passed) {
            $passedCount++
        }
    }
    
    Write-Host ""
    Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Yellow
    Write-Host "Results: $passedCount / $totalCount questions passed" -ForegroundColor Yellow
    Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Yellow
    Write-Host ""
    
    # Exit with appropriate code
    if ($passedCount -eq $totalCount) {
        Write-Success "🎉 All questions passed successfully!"
        exit 0
    }
    else {
        Write-Failure "⚠ Some questions failed. Please review the output above."
        exit 1
    }
}

# Run the main function
Main
