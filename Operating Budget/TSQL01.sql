USE Maryland;

SELECT
    fiscal_year,           -- The budget year (2018)
    agency_name,           -- Which state agency (e.g., Department of Health)
    program_name,          -- Specific program (Office of Administration)
    unit_name,             -- Organizational unit name
    category_title,        -- Budget category (e.g., Salaries, Equipment, Services)
    fund_type_name,        -- Type of funding (e.g., General Fund, Special Fund)
    fund_source_name,      -- Specific source of money
    description,           -- Detailed line item description
    budget                 -- Dollar amount allocated
    FROM dbo.OperatingBudget
   WHERE fiscal_year = 2018
  AND unit_code = 'B01'
  AND program_name = 'Office of Administration'

-- SELECT
--     fiscal_year,   
--     agency_name,   
--     program_name, 
--     unit_name,
--     category_title,
--     fund_type_name,  
--     fund_source_name, 
--     description,
--     budget
-- FROM dbo.OperatingBudget
-- WHERE fiscal_year=2018
-- AND unit_code='B01'
-- AND program_name='Office of Administration'