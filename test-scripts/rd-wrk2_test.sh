echo "wrk -t4 -c120 -d5m -R100 --latency --timeout 2s" >> ./test-results/rd_wrk2_test.txt
for i in {1..5}; do wrk -t4 -c120 -d5m -R100 --latency --timeout 2s [URL TO API-SERVICE] >> ./test-results/rd_wrk2_test.txt; done
echo "wrk -t4 -c120 -d5m -R200 --latency --timeout 2s" >> ./test-results/rd_wrk2_test.txt
for i in {1..5}; do wrk -t4 -c120 -d5m -R200 --latency --timeout 2s [URL TO API-SERVICE] >> ./test-results/rd_wrk2_test.txt; done
echo "wrk -t4 -c120 -d5m -R300 --latency --timeout 2s" >> ./test-results/rd_wrk2_test.txt
for i in {1..5}; do wrk -t4 -c120 -d5m -R300 --latency --timeout 2s [URL TO API-SERVICE] >> ./test-results/rd_wrk2_test.txt; done
echo "wrk -t4 -c120 -d5m -R400 --latency --timeout 2s" >> ./test-results/rd_wrk2_test.txt
for i in {1..5}; do wrk -t4 -c120 -d5m -R400 --latency --timeout 2s [URL TO API-SERVICE] >> ./test-results/rd_wrk2_test.txt; done
echo "wrk -t4 -c120 -d5m -R500 --latency --timeout 2s" >> ./test-results/rd_wrk2_test.txt
for i in {1..5}; do wrk -t4 -c120 -d5m -R500 --latency --timeout 2s [URL TO API-SERVICE] >> ./test-results/rd_wrk2_test.txt; done
echo "wrk -t4 -c120 -d5m -R600 --latency --timeout 2s" >> ./test-results/rd_wrk2_test.txt
for i in {1..5}; do wrk -t4 -c120 -d5m -R600 --latency --timeout 2s [URL TO API-SERVICE] >> ./test-results/rd_wrk2_test.txt; done
echo "wrk -t4 -c120 -d5m -R700 --latency --timeout 2s" >> ./test-results/rd_wrk2_test.txt
for i in {1..5}; do wrk -t4 -c120 -d5m -R700 --latency --timeout 2s [URL TO API-SERVICE] >> ./test-results/rd_wrk2_test.txt; done
echo "wrk -t4 -c120 -d5m -R800 --latency --timeout 2s" >> ./test-results/rd_wrk2_test.txt
for i in {1..5}; do wrk -t4 -c120 -d5m -R800 --latency --timeout 2s [URL TO API-SERVICE] >> ./test-results/rd_wrk2_test.txt; done
echo "wrk -t4 -c120 -d5m -R900 --latency --timeout 2s" >> ./test-results/rd_wrk2_test.txt
for i in {1..5}; do wrk -t4 -c120 -d5m -R900 --latency --timeout 2s [URL TO API-SERVICE] >> ./test-results/rd_wrk2_test.txt; done
echo "wrk -t4 -c120 -d5m -R1000 --latency --timeout 2s" >> ./test-results/rd_wrk2_test.txt
for i in {1..5}; do wrk -t4 -c120 -d5m -R1000 --latency --timeout 2s [URL TO API-SERVICE] >> ./test-results/rd_wrk2_test.txt; done