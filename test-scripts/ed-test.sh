echo "wrk -t4 -c4 -d5m --latency --timeout 2s" >> ./test-results/ed_tests.txt
for i in {1..5}; do wrk -t4 -c4 -d5m --latency --timeout 2s [URL TO API-SERVICE] >> ./test-results/ed_tests.txt; done
echo "wrk -t4 -c40 -d5m --latency --timeout 2s" >> ./test-results/ed_tests.txt
for i in {1..5}; do wrk -t4 -c40 -d5m --latency --timeout 2s [URL TO API-SERVICE] >> ./test-results/ed_tests.txt; done
echo "wrk -t4 -c120 -d5m --latency --timeout 2s" >> ./test-results/ed_tests.txt
for i in {1..5}; do wrk -t4 -c120 -d5m --latency --timeout 2s [URL TO API-SERVICE] >> ./test-results/ed_tests.txt; done
echo "wrk -t4 -c200 -d5m --latency --timeout 2s" >> ./test-results/ed_tests.txt
for i in {1..5}; do wrk -t4 -c200 -d5m --latency --timeout 2s [URL TO API-SERVICE] >> ./test-results/ed_tests.txt; done
echo "wrk -t4 -c280 -d5m --latency --timeout 2s" >> ./test-results/ed_tests.txt
for i in {1..5}; do wrk -t4 -c280 -d5m --latency --timeout 2s [URL TO API-SERVICE] >> ./test-results/ed_tests.txt; done
echo "wrk -t4 -c360 -d5m --latency --timeout 2s" >> ./test-results/ed_tests.txt
for i in {1..5}; do wrk -t4 -c360 -d5m --latency --timeout 2s [URL TO API-SERVICE] >> ./test-results/ed_tests.txt; done
echo "wrk -t4 -c440 -d5m --latency --timeout 2s" >> ./test-results/ed_tests.txt
for i in {1..5}; do wrk -t4 -c440 -d5m --latency --timeout 2s [URL TO API-SERVICE] >> ./test-results/ed_tests.txt; done
echo "wrk -t4 -c520 -d5m --latency --timeout 2s" >> ./test-results/ed_tests.txt
for i in {1..5}; do wrk -t4 -c520 -d5m --latency --timeout 2s [URL TO API-SERVICE] >> ./test-results/ed_tests.txt; done
echo "wrk -t4 -c600 -d5m --latency --timeout 2s" >> ./test-results/ed_tests.txt
for i in {1..5}; do wrk -t4 -c600 -d5m --latency --timeout 2s [URL TO API-SERVICE] >> ./test-results/ed_tests.txt; done
echo "wrk -t4 -c680 -d5m --latency --timeout 2s" >> ./test-results/ed_tests.txt
for i in {1..5}; do wrk -t4 -c680 -d5m --latency --timeout 2s [URL TO API-SERVICE] >> ./test-results/ed_tests.txt; done