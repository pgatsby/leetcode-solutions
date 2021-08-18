# Peter Gatsby
# Problem: https://leetcode.com/explore/interview/card/google/67/sql-2/472/

s = "5F3Z-2e-9-w"
k = 2 

def LicenseKeyFormatting(s, k):
    license_key = s.replace('-', '').upper()
    license_key = license_key[::-1]

    output = []

    for i in range(0, len(license_key), k):
        output.append(license_key[i:i+k])

    output = '-'.join(output)
    output = output[::-1]

    return output

print(LicenseKeyFormatting(s,k))