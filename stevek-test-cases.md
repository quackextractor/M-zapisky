### **[PersonalCloud](https://github.com/Stevekk11/PersonalCloud) Project Testing Report**

* **Tester Name:** Miro Slezák 
* **Environment:** deployed production [website](https://veghtp.dev.spsejecna.net/)

---

### **1. Authentication & User Management**

*   **TC-1.01: User Registration**
    *   **Action:** Register a new account using the Registration UI.
    *   **Expected Result:** Account is created successfully and the user is logged in automatically.
    *   **Status:** Pass
    *   **Notes:** Password requirements validation is inconsistent. After fulfilling some of the checks (between 8 and 100 chars) the user is prompted to fulfill another set of requiremnents such as alphanumeric characters. I found this quite frustrating

*   **TC-1.02: User Login**
    *   **Action:** Attempt to log in with valid credentials.
    *   **Expected Result:** User is successfully authenticated and redirected to the dashboard.
    *   **Status:** Pass

*   **TC-1.03: Premium Status Allocation**
    *   **Action:** Attempt to upgrade an account to Premium.
    *   **Expected Result:** Since the application does not have a UI for this yet, verify that Premium status (`IsPremium`) can only be successfully set manually directly in the SQLite database.
    *   **Status:** Pass 
---

### **2. Document Storage & Quota Management**

*   **TC-2.01: Standard User Quota**
    *   **Action:** Upload files as a standard user until the storage limit is reached.
    *   **Expected Result:** Uploads should be blocked with an `InvalidOperationException` once the 10 GB limit is exceeded.
    *   **Status:** Unknown
    *   **Notes:** Due to the slow upload speed and limits on how much I can upload at once (see TC-3.01)

*   **TC-2.02: Storage Analytics UI**
    *   **Action:** Navigate to the dashboard and review the storage progress bar.
    *   **Expected Result:** The `StorageUsageViewComponent` should correctly calculate used bytes, maximum bytes, and display the accurate usage percentage.
    *   **Status:** Pass
---

### **3. File Uploads, Downloads, and Restrictions**

*   **TC-3.01: Maximum File Size Limit**
    *   **Action:** Attempt to upload a file larger than 5 GB.
    *   **Expected Result:** The system should block the upload due to the configured Kestrel and `FormOptions` maximum body length limits of 5 GB.
    *   **Actual Result:** Page crashed with `PR_CONNECT_RESET_ERROR`
    *   **Status:** Blocked
    *   **Notes:** I had big problems uploading files larger than 200MB (100MB was fine, but anything bigger would take much longer and start to timeout)
*   **TC-3.02: Blocked File Extensions**
    *   **Action:** Attempt to upload restricted file types, such as `.cs`, `.exe`, `.dll`, `.config`, or `.json`.
    *   **Expected Result:** The application should throw an `ArgumentException` or change the content type to `application/octet-stream` to prevent execution.
    *   **Status:** Pass
    *   **Notes:** It took very long (~50 seconds for a 10 mB file)

*   **TC-3.03: Document Deletion**
    *   **Action:** Delete an existing document from the web interface.
    *   **Expected Result:** The file should be permanently removed from both the SQLite database and the physical `UserDocs/` directory on the disk.
    *   **Status:** Pass

---

### **4. Document Preview & Media Galleries**

*   **TC-4.01: Office Document Conversion**
    *   **Action:** Click the "Preview" option on an uploaded `.docx`, `.xlsx`, or `.pptx` file.
    *   **Expected Result:** The file should be successfully converted to a PDF stream in-memory using the Syncfusion rendering engines (requires configured valid license key).
    *   **Actual Result:** 
    - xlsx, pptx file fails with `An unhandled exception occurred while processing the request.
DllNotFoundException: Unable to load shared library 'libSkiaSharp' or one of its dependencies.`
    *   **Status:** Fail

*   **TC-4.02: Image Gallery Filter**
    *   **Action:** Navigate to the Image Gallery route (`/Document/Gallery`).
    *   **Expected Result:** Only supported image formats (jpeg, jpg, png, gif, webp, bmp) should be displayed.
    *   **Status:** Pass

*   **TC-4.03: Music Library Filter**
    *   **Action:** Navigate to the Music Library route (`/Document/Music`).
    *   **Expected Result:** Only supported audio formats (mpeg, mp3, wav, wma, ogg) should be displayed and playable directly in the browser.
     *   **Status:** Pass
---

### **5. Localization**

*   **TC-5.01: Language Switching**
    *   **Action:** Append `?culture=en` or `?culture=cs` to any application URL.
    *   **Expected Result:** The UI should successfully switch between English and Czech languages utilizing the built-in resource files.
    *   **Status:** Pass