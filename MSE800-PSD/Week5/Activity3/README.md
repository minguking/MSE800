# Week 5 – Activity 3: Clinic Management System Activity Diagram

## Overview

This activity diagram models the workflow of a **Clinic Management System**, covering three core processes: appointment booking, medical consultation, and prescription processing.

---

## Description

The system involves three actors working across distinct swim lanes:

| Actor | Role |
|---|---|
| **Patient** | Submits appointment requests, attends consultation, and makes payment |
| **Doctor** | Reviews and approves appointment requests, conducts consultation, and issues prescriptions |
| **Receptionist** | Handles invoicing, payment processing, insurance, and forwards prescriptions to pharmacy |

### Workflow Summary

1. **Appointment Booking** — The patient submits a request with symptoms and preferred doctor. The doctor reviews and either approves or rejects it. If rejected, the patient resubmits with updated details.

2. **Medical Consultation** — Once the appointment is confirmed, the patient attends the consultation. The doctor determines whether a prescription is required or if health advice alone is sufficient.

3. **Prescription & Payment Processing** — The receptionist calculates charges, applies insurance discounts if applicable, and requests payment from the patient. Upon successful payment, the prescription is forwarded to the pharmacy and the patient record is updated.

---

## Key Decision Points

- **Approve Request?** — Doctor may reject if details are insufficient
- **Prescription Needed?** — Determines whether medication or advice only is issued
- **Insurance Applicable?** — Discount applied before payment is requested
- **Payment Successful?** — Patient retries if payment fails
