from jira import JIRA
from openpyxl import Workbook
import os
from datetime import datetime

# Get environment variables for Jira configuration
jira_url = os.environ.get('JIRA_URL')
jira_username = os.environ.get('JIRA_USERNAME')
jira_password = os.environ.get('JIRA_PASSWORD')

print(f"JIRA_URL: {os.environ.get('JIRA_URL_CREDENTIAL_ID')}")
print(f"JIRA_USERNAME: {os.environ.get('JIRA_USERNAME_CREDENTIAL_ID')}")
print(f"JIRA_PASSWORD: {os.environ.get('JIRA_PASSWORD_CREDENTIAL_ID')}")

# Set up Jira connection
jira = JIRA(server=jira_url, basic_auth=(jira_username, jira_password))

# Use the provided parameter directly as the project ID
project_id = os.environ.get('PROJECT_ID')

# Construct JQL query to fetch issues from the specified project
jql_query = f'project = {project_id}'

# Fetch issues based on the JQL query
issues = jira.search_issues(jql_query)


# Create a new Excel workbook and sheet
workbook = Workbook()
sheet = workbook.active

# Write column headers
headers = ['Issue Link','Description', 'Criterion', "Element", "Check type", "Responsibility", "Severity", "Complexity", 'Status', "Last Modified", "Barrier Status", "Branch/Code Location", "QA Status", "UAT Status" ]
sheet.append(headers)

# Write issue data to the sheet
for issue in issues:
    custom_field = issue.raw['fields'].get('customfield_10089', '')
    description = issue.fields.description or ''
    
    Criterion = issue.fields.customfield_10106 or ''
    Element = issue.fields.customfield_10091 or ''
    
    Check_type_field = issue.fields.customfield_10092
    Check_type = Check_type_field.value if Check_type_field else ''

    Responsibility_field = issue.fields.customfield_10093
    Responsibility = Responsibility_field.value if Responsibility_field else ''

    Severity_field = issue.fields.customfield_10094
    Severity = Severity_field.value if Severity_field else ''

    Complexity_field = issue.fields.customfield_10095
    Complexity = Complexity_field.value if Complexity_field else ''
    
    status = issue.fields.status.name
    
    updated_str = issue.fields.updated
    updated = datetime.strptime(updated_str, "%Y-%m-%dT%H:%M:%S.%f%z").strftime("%B %d, %Y %I:%M %p")
    
    barrier_status_field = issue.fields.customfield_10098
    barrier_status = barrier_status_field.value if barrier_status_field else ''
    
    branch_code_located = issue.raw['fields'].get('customfield_10097', '')
    
    qa_validation_status_field = issue.fields.customfield_10102
    qa_validation_status = qa_validation_status_field.value if qa_validation_status_field else ''
    
    uat_validation_status_field = issue.fields.customfield_10103
    uat_validation_status = uat_validation_status_field.value if uat_validation_status_field else ''
    
    # Generate HYPERLINK formula for the Issue Link
    if custom_field:
        issue_url = issue.permalink()
        issue_link_formula = f'=HYPERLINK("{issue_url}", "{custom_field}")'
    else:
        issue_link_formula = ''

    row_data = [issue_link_formula, description, Criterion, Element, Check_type, Responsibility, Severity, Complexity, status, updated, barrier_status, branch_code_located, qa_validation_status, uat_validation_status]
    print(row_data)
    sheet.append(row_data)

# Save the Excel file
excel_file = 'jira_issues.xlsx'
workbook.save(excel_file)

print(f'Jira issues exported to {excel_file}')
