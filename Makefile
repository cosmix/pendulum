
# lists all available targets
list:
	@sh -c "$(MAKE) -p no_targets__ | \
		awk -F':' '/^[a-zA-Z0-9][^\$$#\/\\t=]*:([^=]|$$)/ {\
			split(\$$1,A,/ /);for(i in A)print A[i]\
		}' | grep -v '__\$$' | grep -v 'make\[1\]' | grep -v 'Makefile' | sort"
# required for list
no_targets__:

lint-rust:
	cd rust && cargo fmt --all -- --check
	cd rust && cargo clippy --tests -- -D warnings


format-rust:
	cd rust && cargo fmt --all
	cd rust && cargo clippy --tests --fix --allow-dirty -- -D warnings

dev:
	poetry install --only main --only test --only typing --only build --only lint
	poetry run maturin develop

lint:
	poetry run mypy
	poetry run pre-commit run --all-files

test:
	PENDULUM_EXTENSIONS=0 poetry run pytest -q tests
	poetry run pytest -q tests

clean:
	rm src/pendulum/*.so
