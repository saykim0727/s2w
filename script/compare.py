import sys
import csv
from bindiff import BinDiff
import os

# 인자 처리
if len(sys.argv) != 3:
    print("사용법: python3 compare.py <primary.BinExport> <secondary.BinExport>")
    sys.exit(1)

primary = sys.argv[1]
secondary = sys.argv[2]

# 파일명 추출
primary_file = os.path.basename(primary)
secondary_file = os.path.basename(secondary)

# BinDiff 파일 자동 생성 경로
diff_file = os.path.splitext(primary)[0] + "_vs_" + os.path.splitext(os.path.basename(secondary))[0] + ".BinDiff"
output_csv = os.path.splitext(diff_file)[0] + "_changed.csv"

# BinDiff 로딩
diff = BinDiff(primary, secondary, diff_file)

# CSV 저장
with open(output_csv, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Function Name", f"{primary_file} Addr", f"{secondary_file} Addr", "Similarity"])

    print("변경된 함수 (similarity < 1.00):")
    for primary_func, secondary_func, match in diff.iter_function_matches():
        if match.similarity < 1.0:
            name = secondary_func.name or ""
            addr1 = f"0x{primary_func.addr:X}"
            addr2 = f"0x{secondary_func.addr:X}"
            sim = f"{match.similarity:.4f}"

            print(f"[!] Similarity: {sim}, {name}")
            print(f"    {primary_file} Addr : {addr1}")
            print(f"    {secondary_file} Addr : {addr2}")

            writer.writerow([name, addr1, addr2, sim])

print(f"[+] 변경된 함수 목록 저장 완료: {output_csv}")
