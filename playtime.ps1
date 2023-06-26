
<#
Get a list of shared mailboxes from Exchange online. Create a CSV with the dshared mailboxes name, an members
#>
 
    function Get-ADusermanager {
        param(
            [Parameter(Mandatory=$true)]
            [string]$user
        )
        $manager = (Get-ADUser $user -Properties manager).manager
        if ($manager -eq $null) {
            $manager = "No manager"
        }
        return $manager
    }

# Create test for function Get-ADusermanager

# Import the Active Directory module
Import-Module ActiveDirectory

# Find all disabled AD accounts
Get-ADUser -Filter {Enabled -eq $false} -Properties Name, SamAccountName, UserPrincipalName, Description, EmailAddress, LastLogonDate, PasswordLastSet, AccountExpirationDate, AccountLockoutTime, LockedOut, PasswordNeverExpires, PasswordNotRequired, PasswordExpired