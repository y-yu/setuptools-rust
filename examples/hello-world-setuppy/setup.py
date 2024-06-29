from setuptools import find_packages, setup

from setuptools_rust import Binding, RustExtension, RustBin

try:
    # noinspection PyPackageRequirements,PyUnresolvedReferences
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel

    # noinspection PyPep8Naming,PyAttributeOutsideInit
    class bdist_wheel(_bdist_wheel):
        def finalize_options(self):
            _bdist_wheel.finalize_options(self)
            self.root_is_pure = False

except ImportError:
    bdist_wheel = None

cargo_args = ["--no-default-features"]

setup(
    name="hello-world",
    version="1.0",
    packages=find_packages(where="python"),
    package_dir={"": "python"},
    cmdclass={"bdist_wheel": bdist_wheel},
    rust_extensions=[
        RustBin(
            "helloworldsetuppy",
             args=cargo_args,
             cargo_manifest_args=["--locked"]
        )
    ],
    # rust extensions are not zip safe, just like C-extensions.
    # But `zip_safe=False` is an obsolete config that does not affect how `pip`
    # or `importlib.{resources,metadata}` handle the package.
)
# See reference for RustExtension in https://setuptools-rust.readthedocs.io/en/latest/reference.html
