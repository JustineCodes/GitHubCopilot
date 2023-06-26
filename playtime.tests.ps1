Describe "Get-ADusermanager" {
    BeforeAll {
        # Mock the Get-ADUser cmdlet to return a user object with a manager property
        Mock Get-ADUser { [pscustomobject]@{ manager = "John Doe" } } -ParameterFilter { $Identity -eq "jane.doe" }
    }

    It "Returns the correct manager for a user" {
        # Call the function with a test user
        $manager = Get-ADusermanager -user "jane.doe"

        # Assert that the function returns the correct manager
        $manager | Should Be "John Doe"
    }

    It "Returns 'No manager' for a user with no manager" {
        # Mock the Get-ADUser cmdlet to return a user object with a null manager property
        Mock Get-ADUser { [pscustomobject]@{ manager = $null } } -ParameterFilter { $Identity -eq "jane.doe" }

        # Call the function with a test user
        $manager = Get-ADusermanager -user "jane.doe"

        # Assert that the function returns 'No manager'
        $manager | Should Be "No manager"
    }
}