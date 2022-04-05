import requests as requests

domains = ["account.help-to-save.externaltest.tax.service.gov.uk",
           "account.help-to-save.tax.service.gov.uk",
           "account.help-to-save.service.gov.uk",
           "apply.help-to-save.tax.service.gov.uk",
           "apply.help-to-save.externaltest.tax.service.gov.uk",
           "www.apply-civil-service-apprenticeship.service.gov.uk",
           #"www.apply-civil-service-fast-stream.service.gov.uk",
           "developer.service.hmrc.gov.uk",
           "test-developer.service.hmrc.gov.uk",
           "ida-matching-prod.tax.service.gov.uk"]


def get_amz_cf_id (domains):
    viaISC = []
    noISC = []
    for domain in domains:
        result = requests.get("https://" + domain + "/", headers={"Test":domain}, allow_redirects=False)
        if "X-Amz-Cf-Id" in result.headers:
            viaISC.append(domain)
        else:
            noISC.append(domain)
        print(domain, result.status_code)

    print("Working via ISC:", viaISC)
    print("Not working via ISC:", noISC)


get_amz_cf_id(domains)










