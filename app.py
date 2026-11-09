from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

def parse_matrix(text, name="Matrix"):
    if not text or not text.strip():
        return None
    try:
        lines = text.strip().split('\n')
        matrix = [[float(x) for x in line.strip().split()] for line in lines if line.strip()]
        
        # Check if all rows have equal lengths
        row_len = len(matrix[0])
        for r in matrix:
            if len(r) != row_len:
                return None
        return np.array(matrix)
    except Exception:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    result_title = ""
    result_output = ""
    error_msg = ""
    
    matrix_a_str = request.form.get('matrix_a', '')
    matrix_b_str = request.form.get('matrix_b', '')
    scalar_str = request.form.get('scalar', '2')
    operation = request.form.get('operation', '')

    if request.method == 'POST':
        A = parse_matrix(matrix_a_str, "Matrix A")
        
        if A is None and operation:
            error_msg = "Please enter valid numbers in Matrix A, and ensure all rows have equal elements."
        elif operation:
            try:
                k = float(scalar_str) if scalar_str else 2.0
            except ValueError:
                k = 2.0

            if operation == 'properties':
                rows, cols = A.shape
                is_square = (rows == cols)
                report = [
                    f"• Dimensions (Shape)  : {rows} x {cols}",
                    f"• Total Elements      : {A.size}",
                    f"• Matrix Rank         : {np.linalg.matrix_rank(A)}",
                    f"• Zero Matrix?        : {'Yes' if np.allclose(A, 0) else 'No'}"
                ]
                if is_square:
                    report.append("\n--- Square Matrix Properties ---")
                    det = np.linalg.det(A)
                    report.extend([
                        f"• Determinant (|A|)   : {round(det, 4)}",
                        f"• Invertible?         : {'Yes (Non-Singular)' if not np.isclose(det, 0) else 'No (Singular)'}",
                        f"• Trace               : {round(np.trace(A), 4)}",
                        f"• Symmetric?          : {'Yes (A = A^T)' if np.allclose(A, A.T) else 'No'}",
                        f"• Upper Triangular?   : {'Yes' if np.allclose(A, np.triu(A)) else 'No'}",
                        f"• Lower Triangular?   : {'Yes' if np.allclose(A, np.tril(A)) else 'No'}"
                    ])
                result_title = "Matrix Properties Report"
                result_output = "\n".join(report)

            elif operation == 'add':
                B = parse_matrix(matrix_b_str, "Matrix B")
                if B is not None and A.shape == B.shape:
                    result_title = "Matrix Addition (A + B)"
                    result_output = str(np.add(A, B))
                else:
                    error_msg = "Addition requires Matrix A and Matrix B to have the exact same shape."

            elif operation == 'sub':
                B = parse_matrix(matrix_b_str, "Matrix B")
                if B is not None and A.shape == B.shape:
                    result_title = "Matrix Subtraction (A - B)"
                    result_output = str(np.subtract(A, B))
                else:
                    error_msg = "Subtraction requires Matrix A and Matrix B to have the exact same shape."

            elif operation == 'mul':
                B = parse_matrix(matrix_b_str, "Matrix B")
                if B is not None:
                    try:
                        result_title = "Matrix Multiplication (A * B)"
                        result_output = str(np.dot(A, B))
                    except Exception:
                        error_msg = "Columns of Matrix A must match the rows of Matrix B for multiplication."
                else:
                    error_msg = "Matrix B input is required for multiplication."

            elif operation == 'scalar':
                result_title = f"Scalar Multiplication ({k} * A)"
                result_output = str(np.round(k * A, 4))

            elif operation == 'transpose':
                result_title = "Matrix Transpose (A^T)"
                result_output = str(A.T)

            elif operation == 'determinant':
                if A.shape[0] == A.shape[1]:
                    det = round(np.linalg.det(A), 4)
                    result_title = "Determinant (|A|)"
                    result_output = f"Determinant = {det}"
                else:
                    error_msg = "Determinant is only defined for square matrices."

            elif operation == 'inverse':
                if A.shape[0] == A.shape[1]:
                    try:
                        inv = np.linalg.inv(A)
                        result_title = "Inverse Matrix (A^-1)"
                        result_output = str(np.round(inv, 4))
                    except Exception:
                        error_msg = "Matrix is singular (determinant is 0), inverse does not exist."
                else:
                    error_msg = "Inverse is only defined for square matrices."

            elif operation == 'trace':
                if A.shape[0] == A.shape[1]:
                    result_title = "Trace of Matrix"
                    result_output = f"Trace = {np.trace(A)}"
                else:
                    error_msg = "Trace is only defined for square matrices."

            elif operation == 'eigen':
                if A.shape[0] == A.shape[1]:
                    try:
                        vals, vecs = np.linalg.eig(A)
                        result_title = "Eigenvalues & Eigenvectors"
                        result_output = f"Eigenvalues:\n{np.round(vals, 4)}\n\nEigenvectors (Columns):\n{np.round(vecs, 4)}"
                    except Exception:
                        error_msg = "Could not compute eigenvalues for this matrix."
                else:
                    error_msg = "Eigenvalues are only defined for square matrices."

            elif operation == 'rank':
                result_title = "Rank of Matrix"
                result_output = f"Rank = {np.linalg.matrix_rank(A)}"

    return render_template('index.html', 
                           matrix_a=matrix_a_str, 
                           matrix_b=matrix_b_str, 
                           scalar=scalar_str,
                           result_title=result_title, 
                           result_output=result_output, 
                           error_msg=error_msg)

if __name__ == '__main__':
    app.run(debug=True)